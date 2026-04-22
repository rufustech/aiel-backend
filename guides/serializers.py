from rest_framework import serializers
from .models import Guide


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['id', 'title', 'content', 'guide_type', 'document', 'image', 'year', 'authors', 'created_at', 'updated_at']
