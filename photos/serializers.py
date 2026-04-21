from rest_framework import serializers
from .models import Photo, PhotoGallery
from aiel.html_cleaner import clean_html_content


class PhotoGallerySerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = PhotoGallery
        fields = '__all__'

    def get_description(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.description)


class PhotoSerializer(serializers.ModelSerializer):
    caption = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def get_caption(self, obj):
        """Clean HTML content by removing TinyMCE editor attributes"""
        return clean_html_content(obj.caption)
