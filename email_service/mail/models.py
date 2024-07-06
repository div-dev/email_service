from django.db import models
from django.utils import timezone

class emailRecord(models.Model):
    email= models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    next_interval = models.IntegerField(default=5)
    last_send_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email