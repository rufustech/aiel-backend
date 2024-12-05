from rest_framework import serializers
from .models import Brief

class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brief
        fields = '__all__'
