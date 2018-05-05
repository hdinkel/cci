from django.db import models

# Create your models here.

class Alert(models.Model):
    user_name = models.CharField(max_length=50)  # Should be ForeignKey to User
    user_email = models.EmailField()
    update_time = models.CharField(max_length=2,
            choices=(
                (2, '2 minutes'),
                (10, '10 minutes'),
                (30, '30 minutes'),
                ))
    phrase = models.CharField(max_length=200)
