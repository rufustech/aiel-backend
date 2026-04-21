from rest_framework import viewsets, filters
from .models import Guide
from .serializers import GuideSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'authors', 'content']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by guide_type or year"""
        queryset = Guide.objects.all()
        guide_type = self.request.query_params.get('guide_type', None)
        year = self.request.query_params.get('year', None)

        if guide_type:
            queryset = queryset.filter(guide_type=guide_type)
        if year:
            queryset = queryset.filter(year=year)

        return queryset
