from rest_framework import serializers
from .models import Guide
from aiel.html_cleaner import clean_html_content


class GuideSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = Guide
        fields = '__all__'
    
    def get_content(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.content)
