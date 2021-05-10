from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)

# 게시글 1개당 여러개의 댓글을 달 수 있음
class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 기존 필드 override
    # 첫번째 방법
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 두번째 방법
    # comment_set = CommentListSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
