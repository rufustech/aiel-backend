from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'image', 'fullname', 'position', 'bio','created_at', 'updated_at']
