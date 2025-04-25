from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .filters import BemorFilter
from .models import Bemor
from .serializers import BemorSerializer

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BemorCreateView(generics.CreateAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    permission_classes = [IsAdminUser]


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response



class BemorUpdateView(generics.UpdateAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'uid'
    parser_classes = [MultiPartParser, FormParser]

class BemorDeleteView(generics.DestroyAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class BemorListView(generics.ListAPIView):
    queryset = Bemor.objects.all().order_by('-uid')
    serializer_class = BemorSerializer
    permission_classes = [IsAdminUser]





class BemorSearchView(generics.ListAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = BemorFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="F.I.Sh", type=openapi.TYPE_STRING),
            openapi.Parameter('tugilgan', openapi.IN_QUERY, description="Tug'ilgan sana (YYYY-MM-DD)", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class BemorRetrieveView(generics.RetrieveAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    lookup_field = 'uid'

