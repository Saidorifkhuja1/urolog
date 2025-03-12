import django_filters
from .models import Bemor

class BemorFilter(django_filters.FilterSet):
    tugilgan = django_filters.DateFilter(field_name='tugilgan', lookup_expr='date')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Bemor
        fields = ['name', 'tugilgan']