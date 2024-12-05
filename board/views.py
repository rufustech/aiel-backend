from rest_framework import viewsets
from .models import Board
from .serializers import BoardSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
