from rest_framework import serializers

from .models import *



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
    class Meta:
        model = Shifokor
        fields = ['uid', 'phone_number', 'name', 'category', 'last_name', 'email', 'photo', 'description', 'is_staff']


class ShifokorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifokor
        fields = ['name', 'last_name', 'category', 'email', 'photo']
        read_only_fields = ['phone_number']  # phone_number cannot be updated

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.escription)

        if 'avatar' in validated_data:
            instance.avatar = validated_data['photo']

        instance.save()
        return instance



class ShifokorListSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Shifokor
        fields = ['uid', 'name', 'last_name', 'phone_number', 'email', 'photo', 'category_title', 'description']



# class PasswordResetSerializer(serializers.Serializer):
#     old_password = serializers.CharField(write_only=True)
#     new_password = serializers.CharField(write_only=True)
#
#     class Meta:
#         fields = ['old_password', 'new_password']
#
#     def validate(self, data):
#         if data['old_password'] == data['new_password']:
#             raise serializers.ValidationError("The new password cannot be the same as the old password.")
#         return data