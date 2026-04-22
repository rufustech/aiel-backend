from rest_framework import viewsets, filters
from .models import ResearchHighlight
from .serializers import ResearchHighlightSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ResearchHighlightViewSet(viewsets.ModelViewSet):
    queryset = ResearchHighlight.objects.all()
    serializer_class = ResearchHighlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'content']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by year if provided"""
        queryset = ResearchHighlight.objects.all()
        year = self.request.query_params.get('year', None)
        if year:
            queryset = queryset.filter(created_at__year=year)
        return queryset
    
