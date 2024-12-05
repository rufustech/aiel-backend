from rest_framework import viewsets
from .models import Article, Comment, Category, LikeDislike
from .serializers import ArticleSerializer, CommentSerializer, CategorySerializer, LikeDislikeSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class LikeDislikeViewSet(viewsets.ModelViewSet):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        article = Article.objects.get(id=data['article'])
        user = request.user
        vote = data['vote']

        # Check if user has already liked/disliked this article
        existing_vote = LikeDislike.objects.filter(user=user, article=article)
        if existing_vote.exists():
            existing_vote.update(vote=vote)
            return Response({"message": "Vote updated"}, status=status.HTTP_200_OK)

        # Create a new like/dislike entry
        new_vote = LikeDislike(user=user, article=article, vote=vote)
        new_vote.save()
        return Response({"message": "Vote added"}, status=status.HTTP_201_CREATED)

