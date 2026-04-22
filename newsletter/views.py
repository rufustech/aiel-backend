from rest_framework import viewsets, filters
from .models import Newsletter
from .serializers import NewsLetterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class NewsLetterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsLetterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'authors']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']
