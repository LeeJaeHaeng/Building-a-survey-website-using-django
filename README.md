# Django 설문조사 웹사이트

Django를 사용하여 만든 설문조사 웹사이트입니다.

## 기능
- 설문조사 생성 및 관리
- 객관식, 단답형, 주관식 질문 지원
- 응답자 닉네임 입력
- 실시간 응답 결과 확인

## 설치 방법
1. 저장소 클론
```bash
git clone https://github.com/LeeJaeHaeng/Building-a-survey-website-using-django.git
cd Building-a-survey-website-using-django
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

5. 관리자 계정 생성
```bash
python manage.py createsuperuser
```

6. 서버 실행
```bash
python manage.py runserver
```

## 사용 방법
1. 관리자 페이지(http://localhost:8000/admin)에서 로그인
2. 설문조사 생성 및 질문 추가
3. 설문조사 페이지(http://localhost:8000/polls)에서 응답 수집

## 기술 스택
- Python 3.x
- Django 4.x
- SQLite3
- HTML/CSS
- JavaScript 