"""
Alert models
"""

from django.db import models
from django.urls import reverse

class Alert(models.Model):
    """

    Ebay Alert

    """
    user_name = models.CharField(max_length=50)  # Should be ForeignKey to User
    user_email = models.EmailField()
    update_time = models.CharField(max_length=2, choices=(
        ('2', '2 minutes'), ('10', '10 minutes'), ('30', '30 minutes'),))
    phrase = models.CharField(max_length=200)

    def get_absolute_url(self):
        """
        get_absolute_url important for reverse lookup
        """
        return reverse('alert_edit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.phrase
