### Auth : 기본 CRUD형태에서 계정 생성 및 수정 기능 추가

<hr>

###### 1. settings.py

`AUTH_USER_MODEL = 'accounts.User'` user모델 변경

  

###### 2. admin.py 

`admin.site.register(User, UserAdmin)` 등록

  

###### 3. models.py

User 모델 추가

   

###### 4. forms.py

django.contrib.auth.forms가 기존에 갖고 있던 form 형태를 사용할 수 없어 새로운 form 만들어줌

   

###### #

앱 articles를 migration하기 전에 계정 생성 models.py를 완료한 후 migration을 해야한다. 