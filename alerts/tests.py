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
        """ try to retrieve the alerts """
        client = Client()
        response = client.get('/api/alerts/?format=json')
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


#    def test_delete_alert(self):
#        # get API response
#        response = client.get('/api/alerts/?format=json')
#        alerts = Alert.objects.all()
#        serializer = AlertSerializer(alerts, many=True)
#        self.assertEqual(response.data, serializer.data)
#        self.assertEqual(len(response.data), 3)
#        self.assertEqual(response.status_code, status.HTTP_200_OK)
