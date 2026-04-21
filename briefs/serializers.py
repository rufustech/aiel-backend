from rest_framework import serializers
from .models import Brief
from aiel.html_cleaner import clean_html_content

class BriefSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = Brief
        fields = '__all__'
    
    def get_content(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.content)
