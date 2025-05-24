from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class MyDream(models.Model):
    dream_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.dream_title
    def __str__(self):
        return self.description
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
