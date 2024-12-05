from rest_framework import viewsets
from .models import Brief
from .serializers import BriefSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BriefViewSet(viewsets.ModelViewSet):
    queryset = Brief.objects.all()
    serializer_class = BriefSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
