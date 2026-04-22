from rest_framework import serializers
from .models import MultimediaResource
from aiel.html_cleaner import clean_html_content

class MultimediaResourceSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = MultimediaResource
        fields = ['id', 'title', 'content', 'year', 'authors', 'image', 'created_at', 'updated_at']
    
    def get_content(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.content)
