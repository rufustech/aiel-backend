from rest_framework import viewsets
from .models import MultimediaResource
from .serializers import MultimedaiResourceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MultimediaResourceViewSet(viewsets.ModelViewSet):
    queryset = MultimediaResource.objects.all()
    serializer_class = MultimedaiResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
from rest_framework import viewsets, filters
from .models import MultimediaResource
from .serializers import MultimediaResourceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MultimediaResourceViewSet(viewsets.ModelViewSet):
    queryset = MultimediaResource.objects.all()
    serializer_class = MultimediaResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'authors', 'content']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by year"""
        queryset = MultimediaResource.objects.all()
        year = self.request.query_params.get('year', None)

        if year:
            queryset = queryset.filter(year=year)

        return queryset
    
