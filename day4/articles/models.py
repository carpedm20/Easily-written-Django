from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode

import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()

    class Meta:
        ordering = ["pub_date"]

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
