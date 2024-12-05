from rest_framework import serializers
from .models import Research

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['id', 'title', 'document', 'content', 'year', 'authors', 'footnote', 'image']