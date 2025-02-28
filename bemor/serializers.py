from rest_framework import serializers
from .models import Bemor

class BemorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bemor
        fields = '__all__'
        read_only_fields = ['uid']
