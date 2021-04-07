from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # blank - model field option
    # True일 경우 해당 field는 빈 값을 허용
    # 유효성 검사에서 빈 값이 통과될 수 있음(DB에는 ''가 저장됨)
    image = models.ImageField(blank=True, upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

