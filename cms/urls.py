from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet, CategoryViewSet, LikeDislikeViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet),
router.register(r'likes_dislikes', LikeDislikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
