# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alert
from .serializers import AlertSerializer
from rest_framework import viewsets

# Create your views here.

class AlertList(ListView):
    model = Alert

class AlertCreate(CreateView):
    model = Alert
    success_url = reverse_lazy('alert_list')
    fields = ('user_name', 'user_email', 'phrase', 'update_time')

class AlertUpdate(UpdateView):
    model = Alert
    success_url = reverse_lazy('alert_list')
    fields = ('user_name', 'user_email', 'phrase', 'update_time')

class AlertDelete(DeleteView):
    model = Alert
    success_url = reverse_lazy('alert_list')

class AlertViewSet(viewsets.ModelViewSet):
    """
    API for Alerts
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

#    permission_classes = (IsOwner,)
#    action_permissions = {
#        IsAuthenticated: ['update', 'destroy', 'list', 'create'],
#        AllowAny: ['retrieve']
#    }
