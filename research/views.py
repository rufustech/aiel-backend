from rest_framework import viewsets
from .models import Research
from .serializers import ResearchSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ResearchViewSet(viewsets.ModelViewSet):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
