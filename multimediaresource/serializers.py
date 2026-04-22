from rest_framework import serializers
from .models import MultimediaResource


class MultimediaResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaResource
        fields = ['id', 'title', 'description', 'resource_url', 'resource_type', 'created_at', 'updated_at']
from rest_framework import serializers
from .models import MultimediaResource
from aiel.html_cleaner import clean_html_content

class MultimediaResourceSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = MultimediaResource
        fields = '__all__'
    
    def get_content(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.content)
