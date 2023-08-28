from .models import Scrap
from rest_framework import serializers

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = ('id', 'title', 'description', 'price')