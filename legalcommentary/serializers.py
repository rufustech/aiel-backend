from rest_framework import serializers
from .models import LegalCommentary


class LegalCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalCommentary
        fields = ['id', 'title', 'content', 'year', 'authors', 'image', 'created_at', 'updated_at']
