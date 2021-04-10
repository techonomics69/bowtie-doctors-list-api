"""
Views of Doctors Service
"""
from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters
from .serializers import DoctorSerializer
from .models import Doctor


class NumberRangeFilter(filters.BaseRangeFilter, filters.NumberFilter):
    pass


class DoctorFilter(filters.FilterSet):
    price_range = NumberRangeFilter(field_name='charges__price', lookup_expr='range')
    language = filters.CharFilter(field_name='languages__bcp47', lookup_expr='iexact')
    category = filters.CharFilter(field_name='charges__category', lookup_expr='iexact')

    class Meta:
        model = Doctor
        fields = ['district']


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows doctors to be viewed or edited.
    """
    queryset = Doctor.objects.all().order_by('-name')
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DoctorFilter
