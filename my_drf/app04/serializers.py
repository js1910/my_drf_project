from rest_framework import serializers
from .models import *
from rest_framework.views import APIView
import re

class GameSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Game
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = News
        fields = '__all__'
























