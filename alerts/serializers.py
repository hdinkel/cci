"""
Serializers for Alert module
"""

from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    """
    Serializer for Alert class
    """
    TIME_CHOICES = (
        ('2', '2 minutes'), ('10', '10 minutes'), ('30', '30 minutes'),)

    user_name = serializers.CharField(max_length=50)  # Should be ForeignKey to User
    user_email = serializers.EmailField()
    update_time = serializers.ChoiceField(choices=TIME_CHOICES)
#    update_time = serializers.CharField(max_length=2)

    phrase = serializers.CharField(max_length=200)

    class Meta:
        model = Alert
        fields = ('user_name', 'user_email', 'update_time', 'phrase')
