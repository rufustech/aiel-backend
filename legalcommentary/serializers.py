from rest_framework import serializers
from .models import LegalCommentary

class LegalCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalCommentary
        fields = '__all__'
