from rest_framework import serializers
from .models import Newsletter


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'title', 'content', 'image', 'created_at', 'updated_at']
