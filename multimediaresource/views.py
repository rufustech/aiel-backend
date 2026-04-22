from rest_framework import viewsets, filters
from .models import MultimediaResource
from .serializers import MultimediaResourceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MultimediaResourceViewSet(viewsets.ModelViewSet):
    queryset = MultimediaResource.objects.all()
    serializer_class = MultimediaResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'authors']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']
    
