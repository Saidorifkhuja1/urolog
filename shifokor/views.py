from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from account.utils import unhash_token
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound, AuthenticationFailed
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from account.permissions import IsSuperUser
from rest_framework.parsers import MultiPartParser, FormParser
from account.serializers import PasswordResetSerializer


class ShifokorLoginView(TokenObtainPairView):
    serializer_class = ShifokorLoginSerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ShifokorListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ShifokorListSerializer

    def get_queryset(self):
        category_uid = self.kwargs.get('category_uid')  # Get category UID from URL
        print(f"Filtering for Category UID: {category_uid}")  # Debugging

        queryset = Shifokor.objects.filter(category__uid=category_uid)
        print(f"Queryset: {queryset}")  # Debugging

        return queryset



class ShifokorRegistrationAPIView(generics.CreateAPIView):
    queryset = Shifokor.objects.all()
    serializer_class = ShifokorRegistrationSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()


            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "uid": user.uid,
                "message": "User registered successfully!",
                "refresh": str(refresh),
                "access": access_token
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RetrieveProfileView(generics.RetrieveAPIView):
    serializer_class = ShifokorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uid'

    def get(self, request, *args, **kwargs):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')

        if not user_id:
            raise NotFound("User not found")

        user = get_object_or_404(Shifokor, uid=user_id)
        serializer = self.get_serializer(user)

        return Response(serializer.data)


class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = ShifokorUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uid"

    def get_queryset(self):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')
        return Shifokor.objects.filter(uid=user_id)


class PasswordResetView(APIView):
    queryset = Shifokor.objects.all()
    serializer_class = PasswordResetSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=PasswordResetSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        decoded_token = unhash_token(request.headers)
        user_id = decoded_token.get("user_id")

        if not user_id:
            raise AuthenticationFailed("User ID not found in token")

        old_password = serializer.validated_data.get("old_password")
        new_password = serializer.validated_data.get("new_password")

        user = get_object_or_404(User, uid=user_id)

        if not check_password(old_password, user.password):
            return Response(
                {"error": "Incorrect old password!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.password = make_password(new_password)
        user.save()

        return Response({"data": "Password changed successfully"}, status=status.HTTP_200_OK)


class DeleteProfileAPIView(generics.DestroyAPIView):
    serializer_class = ShifokorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uid'

    def get_queryset(self):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')
        return Shifokor.objects.filter(uid=user_id)

    def perform_destroy(self, instance):

        instance.delete()

    def delete(self, request, *args, **kwargs):

        user = self.get_object()

        self.perform_destroy(user)

        return Response({"message": "User successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
