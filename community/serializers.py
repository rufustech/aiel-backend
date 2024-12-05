from rest_framework import serializers
from .models import Community

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['id', 'image', 'fullname', 'position', 'bio','created_at', 'updated_at']
