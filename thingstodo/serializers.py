# todo/serializers.py

from rest_framework import serializers
from .models import Thingstodo


class ThingstodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thingstodo
        fields = ('id', 'title', 'description', 'completed')
