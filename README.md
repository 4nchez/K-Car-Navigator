# K-Car Navigator
K-Car Navigator 프로젝트는 현대자동차 FAQ 데이터를 크롤링하고, 이를 JSON 파일과 데이터베이스에 저장하여 관리할 수 있는 Python 기반 프로젝트입니다.

---

## 작업자
| 성명 | 이메일 |   
| :--- | :--- |
| 신누리 | 4nchez@gmail.com | 
| 정재희 | jjh2002x@gmail.com | 

## 기능

* 현대자동차 고객센터 FAQ 페이지 크롤링
* 크롤링 데이터를 JSON 파일로 저장
* MySQL 데이터베이스와 연동하여 FAQ 데이터 관리

---

## 요구 사항

* Python 3.10 이상
* MySQL 데이터베이스 8.0 이상
* Python 라이브러리:

```bash
pip install -r requirements.txt
```

---

## `.env` 파일 설정

프로젝트를 실행하려면 루트 디렉토리에 `.env` 파일을 생성하고 아래와 같이 작성하세요.

```dotenv
# Database 설정
DB_HOST={DB 주소}
DB_PORT={DB 포트}
DB_USER={DB 사용자명}
DB_PASSWORD={DB 비밀번호}
DB_NAME=K_Car_Navigator

# 크롤링 관련 설정
CRAWL_URL=https://www.hyundai.com/kr/ko/e/customer/center/faq
JSON_DIR=./data/
```

### 환경 변수 설명

| 변수            | 설명                   |
| ------------- | -------------------- |
| `DB_HOST`     | 데이터베이스 서버 주소         |
| `DB_PORT`     | 데이터베이스 포트            |
| `DB_USER`     | 데이터베이스 사용자명          |
| `DB_PASSWORD` | 데이터베이스 비밀번호          |
| `DB_NAME`     | 사용할 데이터베이스 이름        |
| `CRAWL_URL`   | 크롤링할 FAQ 페이지 URL     |
| `JSON_DIR`    | 크롤링 결과 JSON 파일 저장 경로 |

---

## 크롤링 방법

1. `.env` 파일 설정 완료
2. 데이터베이스 준비
3. 크롤링 스크립트 실행:

```bash
python -m test.crawl_faq.py
```

4. 결과 확인 (`JSON_DIR` 폴더 또는 DB)

---

## 프로젝트 구조
```
K-Car_Navigator/
|   __init__.py
|   .env
|   .gitignore
|   README.md
|   requirements.txt
|
+---common
|       __init__.py
|       logger.py
|       mapper.py
|
+---crawling
|       __init__.py
|       crawling_hyundai_faq.py
|
+---data
|       2026년_4월_자동차_등록자료_통계.xlsx
|
+---database
|       __init__.py
|       db.py
|       db_service.py
|       erd.png
|       init.sql
|
+---document
|       프로젝트_기획초안.txt
|       화면설계서_v0.1.pptx
|
+---models
|       __init__.py
|       dto.py
|       entity.py
|       models.py
|
+---test
|       __init__.py
|       test_crawl_faq.py
|       test_mapper.py
|       test_sql.py
```


## Authors

- **신누리 (Shin Noo Ri)** - [@깃허브아이디](https://github.com/4nchez) - [이메일](mailto:4nchez@gmail.com)
