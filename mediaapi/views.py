from rest_framework import viewsets
from .models import Mediaapi
from .serializers import MediaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Mediaapi.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
