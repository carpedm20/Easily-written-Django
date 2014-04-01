from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode

import datetime

class SignUp(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	
	email = models.EmailField()

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		ordering = ["timestamp"]

	def __unicode__(self):
		return smart_unicode(self.email)

	def was_updated_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.updated < now

	was_updated_recently.admin_order_field = 'updated'
	was_updated_recently.boolean = True
	was_updated_recently.short_description = 'Published recently?'
