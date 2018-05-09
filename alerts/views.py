"""
Django views for alerts
"""

# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .models import Alert
from .forms import AlertForm
from .serializers import AlertSerializer

# Create your views here.

class AlertModelFormView():
    """
    ModelFormView for Alerts, allowing creating and editing Alerts
    """
    alert = Alert.objects.get(pk=3)
    form = AlertForm(instance=alert)


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
