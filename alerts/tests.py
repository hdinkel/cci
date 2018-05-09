"""
Tests for Alerts
"""
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Alert
from .serializers import AlertSerializer
from .management.commands.send_emails import ebay_search


class AccountTests(APITestCase):
    """
    Test module to test the creation of alerts
    """

    def test_create_account(self):
        """
        Ensure we can create a new alert object.
        """
        url = '/api/alerts/'
        data = {'user_name': 'Hans', 'user_email': 'hans@home.de',
                'phrase': 'windows xp', 'update_time': '30'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Alert.objects.count(), 1)
        self.assertEqual(Alert.objects.get().user_name, 'Hans')


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

    def test_create_alert_fails(self):
        """ try to create an alert with an error"""
        response = self.client.post('/api/alerts/',
                                    {'user_name': 'Hans',
                                     'user_email': 'this is no email',
                                     'phrase': 'windows xp',
                                     'update_time': '30'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        alert_count = Alert.objects.count()
        self.assertEqual(alert_count, 3)

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

    def test_ebay_search(self):
        """ try to run the ebay search """
        search = ebay_search('apple')
        self.assertEqual(len(search), 100)

    def test_ebay_search_fails(self):
        """ try to run the ebay search """
        from django.conf import settings
        settings.EBAY_API_KEY = ''
        search = ebay_search('apple')
        self.assertEqual(search, None)
