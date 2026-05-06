# Likelion 14th — Study Platform Toy Project

멋쟁이사자처럼 14기 백엔드 스터디를 위한 종합 토이 프로젝트입니다. FastAPI를 기반으로 커뮤니티(게시판) 및 스터디룸 예약 시스템을 구축하며, 점진적인 주차별 목표를 통해 백엔드의 핵심 개념들을 실습합니다.

---

## 🎯 Week 4 목표: 인증/인가(Auth) 업그레이드 가이드

이번 4주차의 주요 목표는 보안을 강화하고 JWT를 통한 토큰 기반 인증 및 역할(Role) 기반의 인가 처리를 도입하는 것입니다.

### 핵심 구현 내용
1. **패키지 환경 설정**: `bcrypt`, `python-jose[cryptography]` 도입
2. **모델 확장**: `users` 테이블에 권한 계층 처리를 위한 `role` 컬럼 추가 (`user` / `admin`)
3. **비밀번호 암호화**: 평문 비밀번호를 단방향 해시(bcrypt) 알고리즘을 이용해 안전하게 저장
4. **JWT 기반 인증 체계**: 로그인 성공 시 `access_token` 발급
5. **FastAPI 의존성 주입(Dependency Injection)**: 
    - `get_current_user`: 요청마다 Bearer 헤더의 토큰을 검증해 현재 사용자 확인
    - `require_admin`: 관리자 권한이 필요한 API (ex: 스터디룸 생성/수정/삭제 등) 접근 제어
6. **API 보호 적용**: 라우터의 기존 `user_id` 파라미터를 제거하고 의존성 주입을 통해 보안 결함 해결

---

## 🛠️ 기술 스택 (Tech Stack)

- **Framework**: FastAPI
- **Database**: PostgreSQL (Supabase)
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens), passlib (bcrypt)
- **Data Validation**: Pydantic

---

## 🚀 아키텍처 및 폴더 구조 (Architecture)

프로젝트는 명확한 관심사 분리(Separation of Concerns)를 위해 계층형 아키텍처를 따릅니다.

- **Router Layer** (`app/routers/`): 엔드포인트 정의, HTTP 요청 및 응답 처리, 인증 의존성 주입
- **Service Layer** (`app/services/`): 핵심 비즈니스 로직 및 규칙 처리 (해싱, 토큰 발급, 데이터 검증)
- **Repository Layer** (`app/repositories/`): 데이터베이스 쿼리 및 트랜잭션 등 데이터 접근(DAO) 담당
- **Model & Schema Layer** (`app/models/`, `app/schemas/`): SQLAlchemy DB 모델 및 Pydantic 데이터 검증 스키마

---

## ⚙️ 실행 방법 (How to run)

### 1. 가상환경 설정 및 패키지 설치
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 2. 환경변수 설정
`backend/.env.example` 파일을 참고하여 `backend/.env` 파일을 생성하고 Supabase DB URL 및 JWT 시크릿 키 등을 입력합니다.

### 3. 서버 실행
```bash
uvicorn app.main:app --reload
```
서버가 실행되면 [http://localhost:8000/docs](http://localhost:8000/docs) 에 접속하여 Swagger UI를 통해 모든 API를 테스트할 수 있습니다.

---

## 📚 주요 기능 (Features)

1. **사용자 관리**: 회원가입, 로그인, 토큰 인증
2. **게시판 커뮤니티**: 게시글 CRUD, 댓글, 좋아요 기능, 이미지 업로드
3. **스터디룸 관리**: 관리자 권한을 통한 룸 개설 및 설정 (운영 시간/슬롯 제한) 관리
4. **예약 시스템**: 다중 테이블 조인을 활용한 안전한 예약 생성 및 중복/겹침 체크
5. **스터디 그룹**: 그룹 생성, 멤버 초대 및 관리
