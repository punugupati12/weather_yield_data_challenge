from weather_app.models import Weather, Statistics
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class WeatherTestCase(APITestCase):
    '''
    @params: APITestCase
    @feature: Testing our Weather Endpoints
    @return: None
    '''
    def test_fetch_weather_data_wx_data(self):
        '''
        @params: None
        @feature: Testing particular Weather Endpoint : station_name="USC001106", date="20000101", max_temp=20, min_temp=19, precipitation=12
        @return: None
        '''
        Weather.objects.create(
            station_name="USC001106", date="20000101", max_temp=20, min_temp=19, precipitation=12)
        response = self.client.get(reverse("weather-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)

class StatisticsTestCase(APITestCase):
    '''
    @params: APITestCase
    @feature: Testing our Statistics Endpoints
    @return: None 
    '''
    def test_fetch_statistics_data(self):
        '''
        @params: None
        @feature: Testing particular Statistics Endpoint : date='2000-01-01', station_name='Test Station', avg_max_temp=10.0, avg_min_temp=05.0, total_acc_ppt=05.0
        @return: None
        '''
        Statistics.objects.create(
            date='2000-01-01',
            station_name='Test Station',
            avg_max_temp=10.0,
            avg_min_temp=05.0,
            total_acc_ppt=05.0
        )
        response = self.client.get(reverse("stats-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)
