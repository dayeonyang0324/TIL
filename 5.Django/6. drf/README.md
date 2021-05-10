#### django rest framework

- serializers.py 파일 생성 후 `from rest_framework import serializers` serializer 작성
- 기존과 다르게 templates 생성 필요없음. 
- urls, views, models, serializers만 작성한 후 Postman으로 확인
- views.py에서 return을 Response로 받으며 decorators는 api_view로 준다.
