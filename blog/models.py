from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink
from django.utils import timezone


class Post(models.Model):                                                                      
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()                                                 
    created_at = models.DateTimeField('Datetime created') 

    def __unicode__(self):
    	return self.title                               
                                                                                          
                                                                                          
class Comment(models.Model):                                                                   
    post = models.ForeignKey(Post)                                                             
    message = models.TextField()                                                               
    created_at = models.DateTimeField('Datetime created')
    def __unicode__(self):
    	return self.message
