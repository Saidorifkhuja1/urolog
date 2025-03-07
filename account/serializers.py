from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from drf_extra_fields.fields import Base64ImageField



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
        fields = ['uid', 'phone_number', 'name', 'last_name', 'email', 'photo', 'is_doctor']


class UserUpdateSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)  # Supports file uploads

    class Meta:
        model = User
        fields = ['uid', 'name', 'last_name', 'phone_number', 'email', 'photo', 'is_active', 'is_admin', 'is_doctor']
        read_only_fields = ['uid', 'is_admin', 'is_doctor']

    def validate_photo(self, value):
        """Allow both base64 and file uploads."""
        if isinstance(value, str):
            return Base64ImageField().to_internal_value(value)
        return value


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
        data["is_doctor"] = self.user.is_doctor
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


