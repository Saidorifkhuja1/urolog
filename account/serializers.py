from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=1)
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['uid', 'name', 'last_name', 'phone_number', 'email', 'photo', 'password']
        read_only_fields = ['uid']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'phone_number', 'name', 'last_name', 'email', 'photo', 'is_staff']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'photo']
        read_only_fields = ['phone_number']  # phone_number cannot be updated

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        if 'avatar' in validated_data:
            instance.avatar = validated_data['photo']

        instance.save()
        return instance





class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        fields = ['old_password', 'new_password']

    def validate(self, data):
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError("The new password cannot be the same as the old password.")
        return data


class Accountlogin(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["is_staff"] = self.user.is_staff
        return data

    class Meta:
        ref_name = "AccountLoginSerializer"

# class SendOTPSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(max_length=21)
#
# class VerifyOTPSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(max_length=21)
#     otp = serializers.CharField(max_length=4)
#


