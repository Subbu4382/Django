from rest_framework import serializers
from .models import Celebrities

class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model=Celebrities
        fields="__all__"