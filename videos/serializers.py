from rest_framework import serializers
from .models import Video
from aiel.html_cleaner import clean_html_content


class VideoSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'

    def get_description(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.description)
