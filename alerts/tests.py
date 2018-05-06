"""
Tests for Alerts
"""
from django.test import TestCase, Client
from rest_framework import status
from .models import Alert
from .serializers import AlertSerializer

class GetAllAlertsTest(TestCase):
    """
    Test module to GET all Alerts via the API
    """

    def setUp(self):
        """ Creating some alerts first """
        self.client = Client()
        Alert.objects.create(
            user_name='Peter',
            user_email='Peter@nowhere.com',
            update_time='2',
            phrase='apple iphone')
        Alert.objects.create(
            user_name='Paul',
            user_email='Paul@home.de',
            update_time='20',
            phrase='Macbook')
        Alert.objects.create(
            user_name='Ringo',
            user_email='Ringo@yahoo.com',
            update_time='30',
            phrase='lego mindstorms')

    def test_get_all_alerts(self):
        """ try to retrieve all alerts """
        response = self.client.get('/api/alerts/?format=json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.json()), 3)

    def test_get_one_alert(self):
        """ try to retrieve individual alerts """
        response = self.client.get('/api/alerts/1/?format=json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        alert = Alert.objects.get(pk=1)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data, serializer.data)

    def test_create_alert(self):
        """ try to create an alert """
        response = self.client.post('/api/alerts/',
                                    {'user_name': 'Hans',
                                     'user_email': 'hans@home.de',
                                     'phrase': 'windows xp',
                                     'update_time': '30'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        alert_count = Alert.objects.count()
        self.assertEqual(alert_count, 4)

    def test_delete_alert(self):
        """ try to delete an alert """
        response = self.client.delete('/api/alerts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        alert_count = Alert.objects.count()
        self.assertEqual(alert_count, 2)
#        alerts = Alert.objects.all()
#        serializer = AlertSerializer(alerts, many=True)
#        self.assertEqual(response.data, serializer.data)
#        self.assertEqual(len(response.data), 3)
