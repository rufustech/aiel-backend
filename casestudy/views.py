from rest_framework import viewsets
from .models import CaseStudy
from .serializers import CaseStudySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
from rest_framework import viewsets, filters
from .models import CaseStudy
from .serializers import CaseStudySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'authors', 'content']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by year"""
        queryset = CaseStudy.objects.all()
        year = self.request.query_params.get('year', None)

        if year:
            queryset = queryset.filter(year=year)

        return queryset
