from rest_framework import viewsets, filters
from .models import LegalCommentary
from .serializers import LegalCommentarySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class LegalCommentaryViewSet(viewsets.ModelViewSet):
    queryset = LegalCommentary.objects.all()
    serializer_class = LegalCommentarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
