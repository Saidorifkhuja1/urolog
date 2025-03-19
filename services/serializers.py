from rest_framework import serializers
from .models import ServicesCategory, Services

class ServicesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesCategory
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    category = ServicesCategorySerializer(read_only=True)

    class Meta:
        model = Services
        fields = '__all__'
