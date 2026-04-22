from rest_framework import serializers
from .models import CaseStudy


class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = ['id', 'title', 'description', 'content', 'image', 'author', 'created_at', 'updated_at']
