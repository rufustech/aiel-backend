from rest_framework import viewsets
from .models import Resource
from .serializers import ResourceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
