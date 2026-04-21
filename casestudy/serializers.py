from rest_framework import serializers
from .models import CaseStudy

class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = '__all__'
from rest_framework import serializers
from .models import CaseStudy
from aiel.html_cleaner import clean_html_content

class CaseStudySerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = CaseStudy
        fields = '__all__'
    
    def get_content(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.content) if obj.content else ""
