

from rest_framework import generics
from .models import ServicesCategory, Services
from .serializers import ServicesCategorySerializer, ServicesSerializer


class ServicesCategoryList(generics.ListAPIView):
    queryset = ServicesCategory.objects.all()
    serializer_class = ServicesCategorySerializer


class ServicesList(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesListByCategoryName(generics.ListAPIView):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Services.objects.filter(category__title__iexact=category_name)
