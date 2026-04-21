from rest_framework import serializers
from .models import Mediaapi

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mediaapi
        fields = '__all__'
