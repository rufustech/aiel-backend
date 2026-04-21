from rest_framework import viewsets, filters
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'speakers', 'description', 'tags']
    ordering_fields = ['created_at', 'year', 'views']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by category, featured status, or year"""
        queryset = Video.objects.all()
        category = self.request.query_params.get('category', None)
        featured = self.request.query_params.get('featured', None)
        year = self.request.query_params.get('year', None)

        if category:
            queryset = queryset.filter(category=category)
        if featured:
            queryset = queryset.filter(featured=featured.lower() == 'true')
        if year:
            queryset = queryset.filter(year=year)

        return queryset
