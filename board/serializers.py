from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'image', 'fullname', 'position', 'bio', 'created_at', 'updated_at']
