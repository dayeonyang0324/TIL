from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # write_only : 시리얼라이징은 하지만 응답에는 포함시키지 않음
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
