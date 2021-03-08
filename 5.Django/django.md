# Django 

#### - django-admin startproject 프로젝트 이름

#### - python manage.py runserver

- 이 명령어를 통해 url로 이동하며 수시로 확인할 수 있음

#### - python manage.py startapp 앱이름

- settings.py의 installed_apps 제일 처음에 생성한 앱이름 작성하기

#### - 프로젝트의 url.py에 path를 추가하기

- `from 앱이름 import views` 입력하기
- 예) `path('index/', views.index),`

#### - 앱의 views에 함수 생성

```
def index(request):
    return render(request, 'index.html')
```

#### - 앱에 `templates` 폴더에 path 에 해당하는 .html 파일을 생성 후 작성



##### !이것만 확인하자!

- urls.py
- views.py
- models.py



