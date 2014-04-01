from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField()

    def __unicode__(self):
        return self.name
