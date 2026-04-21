from rest_framework import viewsets
from .models import Newsletter
from .serializers import NewsLetterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class NewsLetterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsLetterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
