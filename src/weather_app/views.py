from rest_framework import generics
from rest_framework.pagination import PageNumberPagination as pnp
from django_filters.rest_framework import DjangoFilterBackend as dfb
from .models import Weather, Statistics
from .serializers import WeatherModuleSerializers as wms, StatisticsModuleSerializers as sms

class Weather(generics.ListAPIView):
    '''
    @params: generics.ListAPIView
    @feature: Create Weather View Model
    @return: None 
    '''
    queryset = Weather.objects.all().order_by('-date')
    serializer_class = wms
    pagination_class = pnp
    filter_backends = [dfb]
    filterset_fields = ["date", "station_name"]

class Statistics(generics.ListAPIView):
    '''
    @params: generics.ListAPIView
    @feature: Create Statistics View Model
    @return: None 
    '''
    queryset = Statistics.objects.all().order_by('-date')
    serializer_class = sms
    pagination_class = pnp
    filter_backends = [dfb]
    filterset_fields = ["date", "station_name"]
