from rest_framework import serializers
from .models import LegalCommentary


class LegalCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalCommentary
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
