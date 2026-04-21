from rest_framework import viewsets, filters
from .models import Brief
from .serializers import BriefSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BriefViewSet(viewsets.ModelViewSet):
    queryset = Brief.objects.all()
    serializer_class = BriefSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'authors', 'content']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by year"""
        queryset = Brief.objects.all()
        year = self.request.query_params.get('year', None)

        if year:
            queryset = queryset.filter(year=year)

        return queryset
