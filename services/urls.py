from django.urls import path
from .views import *

urlpatterns = [
    path('categories_list/', ServicesCategoryList.as_view(), name='services-category-list'),
    path('services_list/', ServicesList.as_view(), name='services-list'),
    path('services_by_category/<str:category_name>/', ServicesListByCategoryName.as_view(), name='services-by-category-name'),
]
