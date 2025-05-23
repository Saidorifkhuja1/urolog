from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from drf_extra_fields.fields import Base64ImageField



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'





class ShifokorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=1)
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Shifokor
        fields = ['uid', 'name', 'last_name', 'category', 'phone_number', 'email', 'photo', 'password', 'description']
        read_only_fields = ['uid']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Shifokor.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ShifokorProfileSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.title")
    class Meta:
        model = Shifokor
        fields = ['uid', 'phone_number', 'name', 'category', 'last_name', 'email', 'photo', 'description', 'is_staff', 'is_doctor']



class ShifokorUpdateSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Shifokor
        fields = ['uid', 'name', 'last_name', 'phone_number', 'email', 'photo', 'is_admin', 'is_doctor', 'description']
        read_only_fields = ['uid', 'is_admin', 'is_doctor']

    def validate_photo(self, value):
        """Allow both base64 and file uploads."""
        if isinstance(value, str):  # If it's a base64 string
            return Base64ImageField().to_internal_value(value)
        return value  # If it's a file, return as is

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)  # Fixed typo

        if 'photo' in validated_data:
            instance.photo = validated_data['photo']  # Fixed key name

        instance.save()
        return instance



class ShifokorListSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Shifokor
        fields = ['uid', 'name', 'last_name', 'phone_number', 'email', 'photo', 'category_title', 'description']






class ShifokorLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        data["is_doctor"] = user.is_doctor

        return data

    class Meta:
        ref_name = "ShifokorLoginSerializer"


