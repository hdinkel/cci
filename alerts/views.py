"""
Django views for alerts
"""

# from django.shortcuts import render
import datetime
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from rest_framework import viewsets
from .models import Alert
from .serializers import AlertSerializer

# Create your views here.

class AlertList(ListView):  # pylint: disable=too-many-ancestors
    """
    List of Alerts
    """
    model = Alert

class AlertCreate(CreateView):  # pylint: disable=too-many-ancestors
    """
    Create View for Alerts
    """
    model = Alert
    success_url = reverse_lazy('alert_list')
    fields = ('user_name', 'user_email', 'phrase', 'update_time')

class AlertUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    """
    Update View for Alerts
    """
    model = Alert
    success_url = reverse_lazy('alert_list')
    fields = ('user_name', 'user_email', 'phrase', 'update_time')

class AlertDelete(DeleteView):  # pylint: disable=too-many-ancestors
    """
    Delete View for Alerts
    """
    model = Alert
    success_url = reverse_lazy('alert_list')

class AlertViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    API for Alerts

    retrieve:
        Return an alert instance.

    list:
        Return all alerts, ordered by most recently created.

    create:
        Create a new alert.

    delete:
        Remove an existing alert.

    partial_update:
        Patch an existing alert.

    update:
        Update an alert.
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

#    permission_classes = (IsOwner,)
#    action_permissions = {
#        IsAuthenticated: ['update', 'destroy', 'list', 'create'],
#        AllowAny: ['retrieve']
#    }


def ebay_search(keywords):
    """
    Search Ebay for given keywords.
    returns: list of items

    """

    try:
        api = Connection(appid=settings.EBAY_API_KEY, config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': keywords})

        assert response.reply.ack == 'Success'
        assert isinstance(response.reply.timestamp, datetime.datetime)
        assert isinstance(response.reply.searchResult.item, list)
        assert isinstance(response.dict(), dict)
        items = response.reply.searchResult.item[:20]
        return items

    except ConnectionError as error:
        # TO-DO: do something more meaningful with the error:
        print(error)
        print(error.response.dict())
        return None
