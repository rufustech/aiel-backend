from rest_framework import serializers
from .models import Podcast
from aiel.html_cleaner import clean_html_content


class PodcastSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    transcript = serializers.SerializerMethodField()

    class Meta:
        model = Podcast
        fields = '__all__'

    def get_description(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.description)

    def get_transcript(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.transcript) if obj.transcript else ""
