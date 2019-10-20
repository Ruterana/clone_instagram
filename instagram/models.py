
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
      profile_image = models.ImageField(upload_to = 'pictures/')
      bio= models.CharField(max_length=30)

class Image(models.Model):
    image_name= models.CharField(max_length=30)  
    image_caption = models.TextField()
    user= models.ForeignKey(User)
    post = HTMLField()
    image_path = models.ImageField(upload_to = 'pictures/')
    
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def search_by_image_name(cls,search_term):
        image= cls.objects.filter(image__image_name__contains=search_term)
        return image