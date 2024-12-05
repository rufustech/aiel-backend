from rest_framework import serializers
from .models import Article, Comment, Category, LikeDislike

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add any other fields you need


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    article = serializers.SlugRelatedField(slug_field='title', queryset=Article.objects.all())  # Shows category name
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())  # Shows author's username
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'article', 'user']

class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = ['id', 'user', 'article', 'vote', 'created_at']

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())  # Shows category name
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())  # Shows author's username
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'category', 'author', 'created_at', 'comments', 'likes_count', 'dislikes_count']

    def get_likes_count(self, obj):
        return obj.likes_dislikes.filter(vote=1).count()

    def get_dislikes_count(self, obj):
        return obj.likes_dislikes.filter(vote=-1).count()


