# Django 

`python 3.8.7`

### 1. 가상환경 생성 및 적용

- git bash에서 `python -m venv venv`
- vscode 실행 후 `ctrl + shift + p`  venv실행
- `pip install django` 
- requirements.txt file있다면 `pip install -r requirements.txt`

 <br>

### 2. 프로젝트 생성 및 앱 생성

- `django-admin startproject 프로젝트 이름 .`
- `python manag.py runserver` 실행해서 확인
- `python manage.py startapp 앱이름`

- settings.py의 INSTALLED_APPS  맨 앞에 생성한 앱이름 작성하기
- 프로젝트에 `templates`파일 > `프로젝트이름 파일` 생성후 `base.html`만들기
  - bootstrap5 사용하기위해 설치해주고 INSTALLED_APPS에 등록
  - settings.py의 'DIRS'에 `[BASE_DIR / '프로젝트 이름' / 'templates',],` 등록

<br>

### 3. 앱에 urls.py 파일 생성

- 프로젝트 urls.py에는 import path, include 등록 후 `urlpatterns`에 `path('앱이름/', include('앱이름.urls'))`
- 생성된 앱에 마찬가지로 `app_name`과 `urlpatterns` 등록

<br>

### 4. 앱 model, form, views, urls, templates 설정

- models.py 파일 생성 후 모델만들기
  - `python manage.py makemigrations` 파일 생성 후
  - `python manage.py migrate` 명령어로 DB 만들어 저장
  - `admin.py`에 model 등록
- forms.py 파일 생성 후 class 만들기
- urls.py에 app_name 등록 후 urlpatterns 작성
- 해당 views 작성
- 앱 내에 `templates` 폴더 > `앱이름` 폴더 생성 후 .html만들기

  <br>

##### !이것만 확인하자!

- urls.py
- views.py
- models.py

<br>

### #

- 관리자 생성 

```bash
$ python manage.py createsuperuser
```

- 버전 관리

```bash
$ pip freeze > requirements.txt
```

- seed 생성

```bash
# seed 설치 후 settings 등록
$ python manage.py seed (앱이름) --number=(seed 생성 갯수)
```

