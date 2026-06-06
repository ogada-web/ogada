<!-- doc:owner=TWR doc:audience=PLN,COD updated=2026-06-06T15:30:00+09:00 -->
# ogada 배포 가이드 (DEPLOYMENT_GUIDE.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **상태**: 초안 (Draft)  
> **대상 독자**: **DevOps·인프라 담당**, **ogada 플랫폼 운영자** (`platform_admin` 협업), **고객 센터 IT** (`sysadmin` 협업)  
> **기준 문서**: `docs/REQUIREMENTS.md` §1-4, §4, `docs/API_SPEC.md`, `docs/ADMIN_GUIDE.md`, `docs/DATA_RETENTION_POLICY.md`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

---

## 1. 이 가이드에 대하여

### 1-1. 목적

ogada는 전국 주간보호센터·요양기관을 위한 **B2B SaaS 멀티테넌트** 웹 시스템입니다.  
이 문서는 **로컬 개발 환경 구성**, **스테이징·프로덕션 배포**, **데이터베이스 마이그레이션**, **보안 키 관리**, **백업·모니터링** 절차를 설명합니다.

### 1-2. 문서 범위

| 포함 | 제외 |
|------|------|
| Spring Boot 백엔드·React SPA·PostgreSQL 배포 | 현장 업무 조작 (→ `USER_MANUAL.md`) |
| 환경변수·시크릿·TLS·리버스 프록시 | Tenant 온보딩·RBAC 운영 (→ `ADMIN_GUIDE.md`) |
| Flyway DB 마이그레이션·백업·복구 | 식사·알림톡·공단 API 직접 연동 (v1 이후) |
| 클라우드 벤더 무관 배포 패턴 (Docker 기준) | 특정 클라우드 벤더 단일 선택 (구현 단계에서 결정) |

### 1-3. 아키텍처 개요

```
[사용자 브라우저]
       │ HTTPS
       ▼
[리버스 프록시 / CDN]  ── 정적 파일 (React SPA dist/)
       │
       ├── /api/v1/*  ──► [Spring Boot 3.x] :8080
       │                      │
       │                      ├── JWT (RSA) + RBAC
       │                      ├── Flyway 마이그레이션
       │                      └── PII AES-GCM 암호화
       │
       └── /.well-known/jwks.json (JWT 공개키)
              │
              ▼
        [PostgreSQL 15+] :5432
              │
              └── 일 1회 백업 (30일 보관)
```

| 계층 | 기술 | 비고 |
|------|------|------|
| 프론트엔드 | React 18 + Vite 5 SPA | 빌드 산출물 `src/frontend/dist/` |
| 백엔드 | Spring Boot **3.3.1**, Java **17** | REST API Base URL `/api/v1` |
| 데이터베이스 | PostgreSQL | `pgcrypto` 확장, Flyway V1~V34 |
| 인증 | JWT (RS256) + RBAC | access 30분, refresh 7일 |
| 멀티테넌트 | Organization → Branch | `organization_id` 강제 격리 |

> **구현 상태 (2026-06-06)**: 백엔드 Must API·Flyway **V34**·설정·백업 스케줄러 구현됨. 프론트엔드는 역할별 라우팅 골격. **Dockerfile·docker-compose는 저장소에 아직 없음** — 본 문서 §6은 권장 구성 초안입니다.

---

## 2. 사전 요구사항

### 2-1. 소프트웨어

| 구성요소 | 최소 버전 | 용도 |
|----------|----------|------|
| JDK | **17** | Spring Boot 백엔드 빌드·실행 |
| Maven | 3.9+ | 백엔드 패키징 (`mvn package`) |
| Node.js | 20 LTS | 프론트엔드 빌드 |
| npm | 10+ | 의존성 설치·Vite 빌드 |
| PostgreSQL | **15+** | 운영 DB (dev/prod 동일 엔진) |
| Docker (선택) | 24+ | 컨테이너 배포 시 |
| OpenSSL (선택) | — | JWT RSA 키·시크릿 생성 |

### 2-2. 네트워크·포트 (기본값)

| 서비스 | 포트 | 경로 |
|--------|------|------|
| Spring Boot API | `8080` | `/api/v1/*`, `/actuator/health`, `/.well-known/jwks.json` |
| Vite 개발 서버 | `5173` | SPA (개발 전용) |
| PostgreSQL | `5432` | DB 연결 |

프로덕션에서는 **443(HTTPS) 단일 진입점**을 권장합니다. API와 SPA를 동일 도메인에서 서빙하면 CORS·쿠키 이슈를 줄일 수 있습니다.

### 2-3. 리소스 가이드 (초기·파일럿)

REQUIREMENTS §1-2 규모 가정 기준 **최소 권장**:

| 환경 | API 서버 | DB | 비고 |
|------|---------|-----|------|
| 로컬 개발 | 2 vCPU / 4 GB RAM | 1 vCPU / 2 GB RAM | 단일 인스턴스 |
| 파일럿 (2지점) | 2 vCPU / 4 GB RAM | 2 vCPU / 4 GB RAM | 동시 접속 ~20 |
| 1년차 (~50 Tenant) | 4 vCPU / 8 GB RAM × 2 | 4 vCPU / 16 GB RAM (HA) | 수평 확장 검토 |

---

## 3. 로컬 개발 환경

### 3-1. PostgreSQL 준비

```bash
# PostgreSQL 접속 후
CREATE DATABASE ogada;
CREATE USER ogada WITH ENCRYPTED PASSWORD 'ogada';
GRANT ALL PRIVILEGES ON DATABASE ogada TO ogada;

# ogada DB에 접속하여 (V1 마이그레이션에서 자동 실행되지만 수동 확인 시)
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
```

기본 JDBC URL: `jdbc:postgresql://localhost:5432/ogada`

### 3-2. 보안 키 생성 (개발용)

프로덕션과 동일한 변수명을 사용하되, **개발·스테이징·프로덕션 키를 분리**합니다.

```bash
# PII 암호화 키 (AES-GCM, Base64, 32바이트 권장)
openssl rand -base64 32

# QR 토큰 서명 시크릿 (임의 문자열, 32바이트 이상 권장)
openssl rand -base64 32

# JWT RSA 키 쌍 (2048bit)
openssl genrsa -out jwt-private.pem 2048
openssl rsa -in jwt-private.pem -pubout -out jwt-public.pem
```

> **주의**: 키 미설정 시 `JwtKeyConfig`가 **임시(ephemeral) RSA 키**를 생성합니다. 재시작마다 기존 JWT가 무효화되므로 **개발 편의용**이며 프로덕션에서는 금지합니다.

### 3-3. 백엔드 환경변수 (개발)

`src/backend/` 디렉터리에서 아래 변수를 설정한 뒤 실행합니다.

| 변수 | 필수 (prod) | 기본값 | 설명 |
|------|:-----------:|--------|------|
| `DB_URL` | ✅ | `jdbc:postgresql://localhost:5432/ogada` | JDBC 연결 문자열 |
| `DB_USERNAME` | ✅ | `ogada` | DB 사용자 |
| `DB_PASSWORD` | ✅ | `ogada` | DB 비밀번호 |
| `SERVER_PORT` | — | `8080` | API 수신 포트 |
| `JWT_PRIVATE_KEY` | ✅ | (없음 → ephemeral) | RSA 개인키 PEM 전체 |
| `JWT_PUBLIC_KEY` | ✅ | (없음 → ephemeral) | RSA 공개키 PEM 전체 |
| `JWT_ISSUER` | ✅ | `http://localhost:8080` | JWT `iss` 클레임 |
| `JWT_ACCESS_TTL_SECONDS` | — | `1800` | access 토큰 TTL (30분) |
| `JWT_REFRESH_TTL_DAYS` | — | `7` | refresh 토큰 TTL |
| `PII_ENCRYPTION_KEY` | ✅ | (없음) | Base64 AES 키 (16/24/32바이트) |
| `QR_TOKEN_SECRET` | ✅ | (없음) | 지점 QR HMAC 서명 키 |
| `PASSWORD_RESET_TTL_MINUTES` | — | `60` | 비밀번호 재설정 토큰 TTL |
| `BACKUP_STORAGE_DIR` | — | `./data/backups` | Tenant 백업 manifest 저장 경로 |
| `BACKUP_SCHEDULER_ENABLED` | — | `true` | 일 1회 백업 스케줄러 on/off |
| `BACKUP_DAILY_CRON` | — | `0 0 2 * * *` | 백업 실행 cron (기본 02:00) |
| `CLIENT_PHOTOS_DIR` | — | `./data/client-photos` | 이용자 사진 업로드 경로 |

환경변수 설정 예시:

```bash
export DB_URL="jdbc:postgresql://localhost:5432/ogada"
export DB_USERNAME="ogada"
export DB_PASSWORD="ogada"
export PII_ENCRYPTION_KEY="$(openssl rand -base64 32)"
export QR_TOKEN_SECRET="$(openssl rand -base64 32)"
export JWT_PRIVATE_KEY="$(cat jwt-private.pem)"
export JWT_PUBLIC_KEY="$(cat jwt-public.pem)"
export JWT_ISSUER="http://localhost:8080"
```

### 3-4. 백엔드 실행

```bash
cd src/backend
mvn spring-boot:run
```

| 확인 항목 | 명령·URL | 기대 결과 |
|----------|----------|----------|
| API 헬스 | `curl http://localhost:8080/api/v1/health` | `{"status":"UP","service":"ogada-backend",...}` |
| Actuator | `curl http://localhost:8080/actuator/health` | `{"status":"UP"}` |
| JWKS | `curl http://localhost:8080/.well-known/jwks.json` | RSA 공개키 JWK Set |
| Flyway | 애플리케이션 로그 | `V1`~`V34` 마이그레이션 성공 |

Flyway는 `spring.flyway.enabled=true`, `classpath:db/migration` 경로의 SQL을 **애플리케이션 기동 시 자동 적용**합니다. `spring.jpa.hibernate.ddl-auto=validate`이므로 스키마는 Flyway만 변경합니다.

### 3-5. 프론트엔드 실행

```bash
cd src/frontend
npm install
npm run dev
```

| 항목 | 값 |
|------|-----|
| 개발 URL | `http://localhost:5173` |
| 빌드 명령 | `npm run build` |
| 산출물 | `dist/` (정적 HTML·JS·CSS) |

현재 프론트엔드는 API Base URL 환경변수가 **미구현**입니다. 개발 시 Vite 프록시 추가를 권장합니다 (`vite.config.js`):

```javascript
server: {
  port: 5173,
  proxy: {
    "/api": "http://localhost:8080",
    "/.well-known": "http://localhost:8080",
    "/actuator": "http://localhost:8080"
  }
}
```

> 위 프록시 설정은 **문서 권장안**이며, 저장소 반영은 coder 단계에서 수행합니다.

### 3-6. 백엔드 테스트

```bash
cd src/backend
mvn test
```

CI 파이프라인에서도 동일 명령으로 단위·통합 테스트를 실행합니다.

---

## 4. 프로덕션 환경변수·시크릿

### 4-1. 원칙 (rules.md §3)

- 비밀값은 **환경변수** 또는 **시크릿 매니저**(AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault 등)로만 관리합니다.
- `.env`·키 파일·인증서를 **Git에 커밋하지 않습니다**.
- 스테이징·프로덕션 키를 **절대 공유하지 않습니다**.
- `PII_ENCRYPTION_KEY` 변경 시 **기존 암호화 데이터 복호화 불가** — 키 로테이션 절차(§8-3)를 따릅니다.

### 4-2. 프로덕션 필수 변수

| 변수 | 설명 | 프로덕션 값 예시 |
|------|------|-----------------|
| `DB_URL` | Managed PostgreSQL 엔드포인트 | `jdbc:postgresql://db.internal:5432/ogada?sslmode=require` |
| `DB_USERNAME` / `DB_PASSWORD` | DB 자격증명 | 시크릿 매니저 참조 |
| `JWT_PRIVATE_KEY` / `JWT_PUBLIC_KEY` | RSA PEM (멀티 인스턴스 시 **동일 키** 필수) | 시크릿 매니저 |
| `JWT_ISSUER` | 공개 API URL | `https://api.ogada.example.com` |
| `PII_ENCRYPTION_KEY` | AES-GCM Base64 32바이트 | 시크릿 매니저 |
| `QR_TOKEN_SECRET` | QR HMAC 키 | 시크릿 매니저 |
| `SERVER_PORT` | 컨테이너 내부 포트 | `8080` |

### 4-3. JWT Issuer·CORS

- `JWT_ISSUER`는 실제 API 공개 URL과 일치해야 합니다.
- `SecurityConfig`는 Spring CORS 기본값(`Customizer.withDefaults()`)을 사용합니다. 프로덕션에서는 리버스 프록시 뒤 **동일 오리진** 배포를 우선하고, 별도 도메인 SPA 호스팅 시 허용 오리진을 명시적으로 제한합니다.

### 4-4. 공개 엔드포인트 (인증 불필요)

`SecurityConfig` 기준 permit-all 경로:

| 경로 | 용도 |
|------|------|
| `/api/v1/health` | L7 헬스체크 |
| `/actuator/health` | Spring Actuator 헬스 |
| `/.well-known/jwks.json` | JWT 공개키 배포 |
| `/api/v1/auth/login` | 로그인 |
| `/api/v1/auth/refresh` | 토큰 갱신 |
| `/api/v1/auth/password/reset-request` | 비밀번호 재설정 요청 |
| `/api/v1/auth/password/reset` | 비밀번호 재설정 확인 |

그 외 `/api/v1/*`는 `Authorization: Bearer <access_token>` 필수입니다 (API_SPEC §0).

---

## 5. 빌드·패키징

### 5-1. 백엔드 JAR

```bash
cd src/backend
mvn -DskipTests package
# 산출물: target/backend-0.0.1-SNAPSHOT.jar
```

실행:

```bash
java -jar target/backend-0.0.1-SNAPSHOT.jar
```

### 5-2. 프론트엔드 정적 빌드

```bash
cd src/frontend
npm ci
npm run build
# 산출물: dist/
```

프로덕션 API URL은 빌드 시점에 주입하는 것을 권장합니다 (구현 예정):

```bash
# 권장 패턴 (VITE_ 접두사 — coder 구현 후)
VITE_API_BASE_URL=https://api.ogada.example.com/api/v1 npm run build
```

동일 도메인 리버스 프록시 배포 시 상대 경로 `/api/v1`만 사용해도 됩니다.

---

## 5-1. 프로덕션 시크릿 관리 모범 사례 (2026-06-06 신규)

프로덕션 환경에서는 민감한 정보(DB 비밀번호, JWT 키, PII 암호화 키)를 **코드·환경 설정 파일에 직접 기록해서는 안 됩니다**. rules.md §3 준수:

| 방법 | 권장도 | 설명 |
|------|:-----:|------|
| **환경변수** (` .env` 파일) | ⚠️ | 개발 편의용, 프로덕션에서는 금지 (파일 노출 위험) |
| **OS 환경변수** (`export`) | ⚠️ | 프로세스 환경에만 적용, 다중 서버에서 관리 불편 |
| **클라우드 시크릿 서비스** | ✅ | **권장**: AWS Secrets Manager, GCP Secret Manager, NCP Secure Manager |
| **Kubernetes Secret** | ✅ | **권장**: K8s 환경에서 표준 방식 |

### 프로덕션 시크릿 목록

아래 변수는 **절대 코드·로그에 노출되어서는 안 됩니다**.

| 시크릿 | 용도 | 강도 요건 | 보관 위치 |
|------|------|----------|----------|
| `DB_PASSWORD` | PostgreSQL 접속 | 25자+, 특수문자 포함 | 클라우드 시크릿 서비스 |
| `JWT_PRIVATE_KEY` | JWT 서명 | RSA 2048bit | 클라우드 시크릿 서비스 |
| `JWT_PUBLIC_KEY` | JWT 검증 | RSA 2048bit (공개키 가능) | 코드 또는 `.well-known/jwks.json` |
| `PII_ENCRYPTION_KEY` | 주민번호·연락처 암호화 | AES-256 (32바이트 Base64) | 클라우드 시크릿 서비스 |
| `QR_TOKEN_SECRET` | QR 토큰 서명 | 32바이트 이상 | 클라우드 시크릿 서비스 |

### 클라우드 시크릿 서비스 연동 예시 (AWS 기준)

**1단계: Secrets Manager에 시크릿 저장**

```bash
aws secretsmanager create-secret --name /ogada/prod/db-password \
  --secret-string "$(openssl rand -base64 25)"

aws secretsmanager create-secret --name /ogada/prod/jwt-private-key \
  --secret-string "$(cat jwt-private.pem)"

aws secretsmanager create-secret --name /ogada/prod/pii-encryption-key \
  --secret-string "$(openssl rand -base64 32)"
```

**2단계: EC2/ECS 타스크 역할에 `SecretsManagerReadAccess` 권한 부여**

**3단계: 애플리케이션 시작 스크립트에서 시크릿 가져오기**

```bash
#!/bin/bash
export DB_PASSWORD=$(aws secretsmanager get-secret-value --secret-id /ogada/prod/db-password --query SecretString --output text)
export JWT_PRIVATE_KEY=$(aws secretsmanager get-secret-value --secret-id /ogada/prod/jwt-private-key --query SecretString --output text)
export PII_ENCRYPTION_KEY=$(aws secretsmanager get-secret-value --secret-id /ogada/prod/pii-encryption-key --query SecretString --output text)

cd /opt/ogada/backend && java -jar app.jar
```

### 보안 체크리스트

- [ ] `.env`, `secrets.yml` 등 시크릿 파일이 **Git 저장소에 포함되지 않음** (.gitignore 확인)
- [ ] 프로덕션 클라우드 시크릿 서비스에서 **자동 로테이션** 설정 (90일 권장)
- [ ] 시크릿 접근 시 **IAM 로그·감사 로그** 기록 확인
- [ ] 로그·에러 메시지에서 시크릿 값이 **절대 출력되지 않음** (GlobalExceptionHandler에서 검증)
- [ ] 개발·스테이징·프로덕션 시크릿을 **별도 관리** (크로스 환경 사용 금지)

---

## 6. Docker·컨테이너 배포 (권장 초안)

> 저장소에 Dockerfile이 **아직 없습니다**. 아래는 REQUIREMENTS §1-4「Docker + PostgreSQL 이식 가능 구조」에 따른 **권장 초안**입니다. 인프라 구현 시 `deploy/` 디렉터리로 코드화합니다.

### 6-1. docker-compose.yml (개발·스테이징 참고)

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ogada
      POSTGRES_USER: ogada
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ogada -d ogada"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build: ./src/backend
    environment:
      DB_URL: jdbc:postgresql://db:5432/ogada
      DB_USERNAME: ogada
      DB_PASSWORD: ${DB_PASSWORD}
      JWT_PRIVATE_KEY: ${JWT_PRIVATE_KEY}
      JWT_PUBLIC_KEY: ${JWT_PUBLIC_KEY}
      JWT_ISSUER: ${JWT_ISSUER:-http://localhost:8080}
      PII_ENCRYPTION_KEY: ${PII_ENCRYPTION_KEY}
      QR_TOKEN_SECRET: ${QR_TOKEN_SECRET}
    ports:
      - "8080:8080"
    depends_on:
      db:
        condition: service_healthy

  web:
    build: ./src/frontend
    ports:
      - "80:80"
    depends_on:
      - api

volumes:
  pgdata:
```

### 6-2. 백엔드 Dockerfile (권장 초안)

```dockerfile
# src/backend/Dockerfile
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY target/backend-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

멀티스테이지 빌드 시 `maven:3.9-eclipse-temurin-17`로 `mvn package` 후 JAR만 복사합니다.

### 6-3. 프론트엔드 Dockerfile (권장 초안)

```dockerfile
# src/frontend/Dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

### 6-4. Nginx 리버스 프록시 (권장)

SPA와 API를 **단일 도메인**으로 서빙하는 `nginx.conf` 예시:

```nginx
server {
    listen 80;
    server_name ogada.example.com;

    # React SPA
    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }

    # Spring Boot API
    location /api/ {
        proxy_pass http://api:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /.well-known/ {
        proxy_pass http://api:8080;
    }

    location /actuator/health {
        proxy_pass http://api:8080;
    }
}
```

프로덕션에서는 **TLS 종료**(Let's Encrypt, ACM, Cloud Load Balancer)를 앞단에 둡니다. REQUIREMENTS §4: **HTTPS 필수**.

---

## 7. 클라우드 배포 패턴 (벤더 무관)

REQUIREMENTS §1-4: AWS / GCP / NCP 등 **벤더 무관**. 공통 패턴만 기술합니다.

### 7-1. 권장 토폴로지

```
[Internet]
    │
[CDN / WAF] (선택)
    │
[Load Balancer] ── TLS 종료
    │
    ├── [Web] Nginx + React dist (또는 S3+CloudFront / GCS+CDN)
    │
    └── [API] Spring Boot × N (오토스케일)
              │
              └── [Managed PostgreSQL] Primary (+ Read Replica, HA)
```

### 7-2. 벤더별 매핑 (참고)

| 역할 | AWS | GCP | NCP |
|------|-----|-----|-----|
| 컴퓨팅 | ECS Fargate / EKS | Cloud Run / GKE | NKS / Server |
| DB | RDS PostgreSQL | Cloud SQL PostgreSQL | Cloud DB for PostgreSQL |
| 시크릿 | Secrets Manager | Secret Manager | Secret Manager |
| 정적 호스팅 | S3 + CloudFront | GCS + Cloud CDN | Object Storage + CDN |
| 백업 | RDS 스냅샷 + S3 | Cloud SQL 백업 + GCS | DB 백업 + Object Storage |

### 7-3. 멀티테넌트 운영 고려

- **단일 DB·단일 스키마** + `organization_id` 행 수준 격리 (현재 구현).
- API 인스턴스는 **무상태(stateless)** — JWT 검증만으로 스케일 아웃 가능.
- `JWT_PRIVATE_KEY`는 모든 API 인스턴스에서 **동일**해야 합니다.
- 파일 업로드(이용자 사진 등) 도입 시 **오브젝트 스토리지** + Tenant별 경로 접두사를 사용합니다.

---

## 8. 데이터베이스 운영

### 8-1. Flyway 마이그레이션

| 버전 | 파일 | 주요 내용 |
|------|------|----------|
| V1 | `V1__init_multi_tenant_schema.sql` | Organization·Branch·User·Client 기본 스키마, `pgcrypto` |
| V2 | `V2__mvp_complement_schema.sql` | MVP 보완 테이블 (보호자·QR·NHIS·청구 라인) |
| V3~V12 | `V3`~`V12` | 인덱스·제약·청구·출석·감사·백업 무결성 |
| V13~V15 | `V13`~`V15` | 건강·copay·QR 도메인, 출석·보존 purge |
| V16~V18 | `V16`~`V18` | 청구 Tenant FK, NHIS 배치 도메인, QR 토큰 값 |
| V19~V20 | `V19`~`V20` | NHIS 대사·백업 종료 상태 무결성 |
| V21~V26 | `V21`~`V26` | NHIS 지점 정렬·Tenant 트리거·청구·출석·보호자 조회 인덱스 |
| V27~V28 | `V27`~`V28` | NHIS·플랫폼·인증·백업 스케줄 조회 성능 인덱스 |
| V29~V31 | `V29`~`V31` | 직원 지점 역조회·사업자번호 검색·이메일 UK·청구 상태·보호자 인덱스 |
| V32~V33 | `V32`~`V33` | actor backstop 트리거·NHIS imported_at·퇴소 purge·활성 이용자 목록 인덱스 |
| V34 | `V34__clients_lifecycle_integrity_and_branch_purge.sql` | 퇴소 시각 ≥ 등록 시각 CHECK, 지점별 `discharged_at` purge 인덱스 |

**V27–V34 요약 (2026-06-06)**

| 버전 | 주요 내용 |
|------|----------|
| V27 | NHIS import 인정번호·지점 조회, 청구 명세·수가표·Tenant명 검색 인덱스 |
| V28 | 이메일 로그인·비밀번호 재설정 조회, NHIS 배치 행·백업 Tenant 스캔 인덱스 |
| V29 | `user_branches` user_id 역조회, 플랫폼 사업자번호 trigram, 청구 라인 정렬 인덱스 |
| V30 | Tenant `lower(email)` UK, 활성 refresh partial, 직원 `(org, is_active)` 인덱스 |
| V31 | 청구 status+`generated_at` 인덱스, 상태 이력 no-op CHECK, 대표 보호자 partial |
| V32 | `ogada_read_actor_user_id()`, 출석·청구 actor 트리거, NHIS `imported_at` backstop, 퇴소 purge partial |
| V33 | 건강·NHIS actor 트리거, client_id purge 인덱스, 활성 이용자 `(org, branch, created_at)` partial |
| V34 | `chk_clients_discharged_after_created`, `idx_clients_org_branch_discharged_at` (지점별 퇴소 cohort) |

**배포 순서**

1. DB 백업 수행 (§8-2)
2. API 인스턴스 기동 → Flyway 자동 마이그레이션
3. 로그에서 `Successfully applied` 확인
4. `/api/v1/health` 및 핵심 API 스모크 테스트
   - `GET /api/v1/billing/claims?status=CONFIRMED` — 청구 상태 필터 (V31 인덱스)
   - `GET /api/v1/billing/imports/nhis/{batchId}` — NHIS 배치 상세·행 매칭 상태
   - 출석·건강 기록 INSERT 후 `created_by`/`recorded_by` NOT NULL 확인 (V32–V33 트리거)

**롤백**: Flyway는 **down 마이그레이션 미포함**. 롤백은 **백업 복원** 또는 **수동 역방향 SQL**로 처리합니다. 스키마 변경 PR에는 롤백 시나리오를 함께 기록합니다.

### 8-2. 백업·복구

| 항목 | 정책 (REQUIREMENTS §4, DATA_RETENTION_POLICY §3) |
|------|--------------------------------------------------|
| 주기 | **일 1회** 전체 DB 스냅샷 |
| 보관 | **30일** 롤링 |
| 암호화 | at-rest 암호화 (KMS·환경변수 키) |
| RPO / RTO | 24시간 / 4시간 (인프라 구현 시 확정) |

**수동 pg_dump 예시**

```bash
pg_dump -h <db-host> -U ogada -Fc ogada > ogada_$(date +%Y%m%d).dump
```

**복구 예시**

```bash
pg_restore -h <db-host> -U ogada -d ogada --clean --if-exists ogada_20260605.dump
```

**ogada 내장 스케줄러** (`BackupRunService`, `BACKUP_SCHEDULER_ENABLED=true`)는 `backupEnabled=true`인 Tenant에 대해 manifest 백업을 실행하고 `backup_runs`에 이력을 남깁니다 (V9, V20).

**프로덕션 권장**: Managed PostgreSQL 자동 스냅샷 + `pg_dump`를 주 백업으로 사용하고, ogada manifest는 보조·점검용으로 운영합니다. `sysadmin`은 `GET /settings/backups`로 이력을 확인합니다.

### 8-3. PII 암호화 키 로테이션

`PII_ENCRYPTION_KEY` 변경은 **재암호화(re-encrypt) 배치** 없이는 기존 데이터를 읽을 수 없습니다.

권장 절차:

1. 유지보수 창구 공지
2. 전체 DB 백업
3. 새 키로 **컬럼 단위 재암호화** 배치 실행 (별도 스크립트·마이그레이션)
4. 애플리케이션 환경변수를 새 키로 전환
5. 검증 후 구 키 폐기

운영 전까지 키 변경 빈도는 **연 1회 이하**를 권장합니다 (`ADMIN_GUIDE.md` §4-6).

---

## 9. 모니터링·헬스체크

### 9-1. 헬스 엔드포인트

| URL | 용도 | LB 프로브 |
|-----|------|----------|
| `GET /api/v1/health` | 애플리케이션 UP/DOWN | ✅ 권장 |
| `GET /actuator/health` | Spring Actuator (DB 포함 가능) | ✅ |
| `GET /.well-known/jwks.json` | JWT 키 배포 확인 | 진단용 |

`management.endpoints.web.exposure.include=health,info` (application.yml 기준).

### 9-2. 로그·알림

| 항목 | 권장 |
|------|------|
| 로그 수집 | stdout → CloudWatch / Cloud Logging / Loki |
| PII | 로그에 주민번호·연락처 **평문 금지** — UUID·마스킹만 |
| 알림 | 5xx 급증, 헬스 실패, DB 연결 실패, 백업 실패 |
| 감사 | `audit_logs` 테이블 + `GET /settings/audit-logs` |

### 9-3. SLA 목표

REQUIREMENTS §4: 가용성 **99.5%** 이상. 월 ~3.6시간 이하 다운타임 허용 범위입니다.

---

## 10. CI/CD 개요

저장소에 파이프라인 정의는 **아직 없습니다**. 권장 단계:

```
[PR] → lint/test (mvn test, npm build)
         │
[merge main] → build JAR + dist
         │
[staging] → Flyway migrate → smoke test (/api/v1/health, POST /auth/login)
         │
[production] → blue-green 또는 rolling deploy → 헬스 확인
```

| 단계 | 검증 |
|------|------|
| 빌드 | `mvn -B test` (22 테스트 클래스), `npm ci && npm run build` |
| 스테이징 | Flyway V1~V34 적용, E2E 로그인·Tenant 격리·청구 상태 필터·NHIS 수동 매칭 |
| 프로덕션 | 헬스·JWKS·백업 스케줄·`BACKUP_STORAGE_DIR` 쓰기 권한 확인 |

---

## 11. 배포 후 검증 체크리스트

### 11-1. 인프라

- [ ] HTTPS 인증서 유효, HTTP → HTTPS 리다이렉트
- [ ] `GET /api/v1/health` → `status: UP`
- [ ] `GET /actuator/health` → `UP`
- [ ] `GET /.well-known/jwks.json` → RSA JWK 반환
- [ ] PostgreSQL TLS (`sslmode=require`) 연결
- [ ] 일 1회 백업 스케줄 동작·30일 보관 확인

### 11-2. 보안

- [ ] `JWT_PRIVATE_KEY`·`PII_ENCRYPTION_KEY`·`QR_TOKEN_SECRET`이 시크릿 매니저에만 존재
- [ ] ephemeral JWT 키 **미사용** (로그에 warn 없음)
- [ ] 에러 응답에 스택·DB 스키마 미노출 (API_SPEC §0-3)
- [ ] 공개 엔드포인트만 permit-all, 나머지 401/403 정상

### 11-3. 기능 스모크 (MVP)

- [ ] `POST /api/v1/auth/login` — 테스트 계정 로그인
- [ ] `GET /api/v1/auth/me` — JWT·역할·`organization_id` 확인
- [ ] `platform_admin` — Tenant 생성 E2E (파일럿 전)
- [ ] 테넌트 A 토큰으로 테넌트 B 데이터 접근 **403** 확인

---

## 12. 장애 대응·트러블슈팅

| 증상 | 가능 원인 | 조치 |
|------|----------|------|
| 기동 실패 `JWT RSA key configuration is invalid` | PEM 형식 오류 | `JWT_PRIVATE_KEY`/`JWT_PUBLIC_KEY` PEM 헤더·줄바꿈 확인 |
| 기동 실패 Flyway | 마이그레이션 충돌·DB 버전 불일치 | `flyway_schema_history` 확인, 백업 후 수동 정합 |
| `500` PII 관련 | `PII_ENCRYPTION_KEY` 미설정·길이 오류 | Base64 32바이트 키 설정 (16/24/32 허용) |
| 로그인 후 즉시 401 | JWT issuer 불일치·키 변경 | `JWT_ISSUER`와 토큰 `iss` 일치, 키 영구 설정 |
| QR 스캔 실패 | `QR_TOKEN_SECRET` 불일치·만료 | 동일 시크릿·서버 시각(NTP) 확인 |
| CORS 오류 | SPA·API 도메인 분리 | §6-4 동일 오리진 프록시 또는 CORS 허용 목록 |
| 느린 응답 | DB 커넥션·인덱스 | PostgreSQL slow query, V3/V6 인덱스 적용 확인 |

장애 시 `sysadmin`은 증상·시각·Tenant ID를 ogada ops에 전달하고, 복구 전후 `audit_logs`에 기록합니다 (`ADMIN_GUIDE.md` §4-4).

---

## 13. 관련 문서

| 문서 | 내용 |
|------|------|
| `docs/REQUIREMENTS.md` | 비기능 요구·배포 원칙 |
| `docs/API_SPEC.md` | REST API·인증 규약 |
| `docs/ADMIN_GUIDE.md` | Tenant 온보딩·백업·보안 키 운영 |
| `docs/DATA_RETENTION_POLICY.md` | 백업 보존·파기 정책 |
| `docs/FLOWCHART.md` | 역할별 화면 흐름 |
| `src/backend/src/main/resources/application.yml` | 런타임 설정 기준 |

---

## 14. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-06 | Flyway V34, 퇴소 시각 CHECK·지점 purge·NHIS 수동 매칭 스모크 테스트 |
| 2026-06-06 | Flyway V32–V33, actor backstop·퇴소 purge·청구 상태 필터 스모크 테스트 |
| 2026-06-06 | Flyway V29–V31, Tenant 이메일 UK·청구 상태 DB·테스트 21클래스 반영 |
| 2026-06-06 | Flyway V21–V28, 조회 성능 인덱스·테스트 19클래스 반영 |
| 2026-06-06 | Flyway V13–V20, 백업·사진 환경변수, 내장 백업 스케줄러 반영 |
| 2026-06-05 | 초안 작성 — 로컬·프로덕션·Docker 권장 구성 |

---

*이 문서는 tech_writer 에이전트가 관리합니다. Dockerfile·CI 추가 시 본 문서와 동기화하세요.*
