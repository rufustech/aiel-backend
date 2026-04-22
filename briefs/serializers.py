from rest_framework import serializers
from .models import Brief


class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brief
        fields = ['id', 'title', 'document', 'content', 'year', 'authors', 'image', 'footnote']
