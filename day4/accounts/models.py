from django.db import models
from django.contrib.auth.models import User

import hashlib

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User)

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()
    def __unicode__(self):
        return self.user

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
