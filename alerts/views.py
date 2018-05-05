# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alert
from .serializers import AlertSerializer
from rest_framework import viewsets
from django.conf import settings

# Create your views here.

class AlertList(ListView):
    """ 
    List of Alerts
    """
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
    import datetime
    from ebaysdk.exception import ConnectionError
    from ebaysdk.finding import Connection

    try:
        api = Connection(appid=settings.EBAY_API_KEY, config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': keywords})

        assert(response.reply.ack == 'Success')
        assert(type(response.reply.timestamp) == datetime.datetime)
        assert(type(response.reply.searchResult.item) == list)
        assert(type(response.dict()) == dict)
        items = response.reply.searchResult.item[:20]
        return(items)

    except ConnectionError as e:
        # TODO: do something more meaningful with the error:
        print(e)
        print(e.response.dict())
        return(None)

if __name__ == '__main__':
    print('\n'.join([i for i in ebay_search('batman')]))
