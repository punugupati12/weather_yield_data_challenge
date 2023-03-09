from rest_framework import serializers
from .models import Weather, Statistics

class WeatherModuleSerializers(serializers.ModelSerializer):
    '''
    @params: serializers.ModelSerializer
    @feature: Create Serializers for Weather Module
    @return: None 
    '''
    class Meta:
        model = Weather
        fields =[ "date" ,"max_temp" ,"min_temp" ,"precipitation" , "station_name" ]

class StatisticsModuleSerializers(serializers.ModelSerializer):
    '''
    @params: serializers.ModelSerializer
    @feature: Create Serializers for Statistics Module
    @return: None 
    '''
    class Meta:
        model = Statistics
        fields =[ "date" ,"total_acc_ppt" ,"avg_min_temp" ,"avg_max_temp" , "station_name" ]