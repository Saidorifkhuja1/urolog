from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [

   path('register/', ShifokorRegistrationAPIView.as_view()),
   path('login/', ShifokorLoginView.as_view()),
   path('shifokor_list/', ShifokorListView.as_view()),
   path('profile_details/', RetrieveProfileView.as_view()),
   path('update_profile/<uuid:uid>/', UpdateProfileView.as_view()),
   path('reset_password/', PasswordResetView.as_view()),
   path('delete_profile/<uuid:uid>/', DeleteProfileAPIView.as_view()),
   path('api/shifokor_by_category/<uuid:category_uid>/', ShifokorListByCategoryAPIView.as_view()),


   path('category_create/', CategoryCreateView.as_view()),
   path('category_list/', CategoryListView.as_view()),


]



