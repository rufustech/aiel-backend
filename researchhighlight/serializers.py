from rest_framework import serializers
from .models import ResearchHighlight

class ResearchHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchHighlight
        fields = '__all__'
