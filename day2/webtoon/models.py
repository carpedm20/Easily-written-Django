from django.db import models
from django.contrib.auth.models import User
 
class Author(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
 
    def __unicode__(self):
        return self.name
 
class Comic(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    desc = models.TextField()
 
    def __unicode__(self):
        return self.title
 
class Episode(models.Model):
    title = models.CharField(max_length=200)
    comic = models.ForeignKey(Comic)
    img_file = models.FileField(upload_to='comics')
    pub_date = models.DateTimeField()
 
    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User)
    msg = models.CharField(max_length=200)
    episode = models.ForeignKey(Episode)
    written_date = models.DateTimeField()
 
    def __unicode__(self):
        return "%s : %s" % ( self.user.username, self.msg )
