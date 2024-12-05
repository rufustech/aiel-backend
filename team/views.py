from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
