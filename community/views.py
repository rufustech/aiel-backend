from rest_framework import viewsets
from .models import Community
from .serializers import CommunitySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
