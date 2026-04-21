from rest_framework import viewsets
from .models import LegalCommentary
from .serializers import LegalCommentarySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LegalCommentaryViewSet(viewsets.ModelViewSet):
    queryset = LegalCommentary.objects.all()
    serializer_class = LegalCommentarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
from rest_framework import viewsets, filters
from .models import LegalCommentary
from .serializers import LegalCommentarySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LegalCommentaryViewSet(viewsets.ModelViewSet):
    queryset = LegalCommentary.objects.all()
    serializer_class = LegalCommentarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'authors', 'content']
    ordering_fields = ['created_at', 'year']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by year"""
        queryset = LegalCommentary.objects.all()
        year = self.request.query_params.get('year', None)

        if year:
            queryset = queryset.filter(year=year)

        return queryset
    
