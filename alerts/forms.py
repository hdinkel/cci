"""
Forms for Alerts
"""
from django.forms import ModelForm
from .models import Alert

class AlertForm(ModelForm):
    """
    ModelForm for Alerts
    """
    class Meta:
        model = Alert
        fields = ('user_name', 'user_email', 'update_time', 'phrase')
