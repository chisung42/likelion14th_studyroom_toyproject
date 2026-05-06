# Week2 사전과제 (FastAPI)

## 완료 내용
- 가상환경 생성: `venv`
- 패키지 설치: `fastapi`, `uvicorn`
- `main.py` 구현
  - `GET /hello`
  - `GET /hello/{name}`
  - `GET /add/{a}/{b}` (선택 과제)

## 실행 방법
```bash
source venv/bin/activate
uvicorn main:app --reload
```

브라우저에서 아래 주소 접속:
- `http://localhost:8000/docs`

## 빠른 확인
- `GET /hello` -> 인사 메시지 반환
- `GET /hello/{name}` -> 이름 환영 메시지 반환
- `GET /add/{a}/{b}` -> 두 수 합 반환
