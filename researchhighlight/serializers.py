from rest_framework import serializers
from .models import ResearchHighlight


class ResearchHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchHighlight
        fields = ['id', 'title', 'description', 'content', 'image', 'author', 'created_at', 'updated_at']
