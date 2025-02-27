from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from account.permissions import IsSuperUser
from .serializers import *


class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsSuperUser]
    parser_classes = [MultiPartParser, FormParser]


    def create(self, request, *args, **kwargs):

        response = super().create(request, *args, **kwargs)


        return response

class NewsRetrieveView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]


class NewsUpdateView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsSuperUser]
    lookup_field = 'uid'
    parser_classes = [MultiPartParser, FormParser]


class NewsDeleteView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'uid'
    permission_classes = [IsSuperUser]


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-uploaded_at')
    serializer_class = NewsSerializer
    # permission_classes = [IsAdminUser]
