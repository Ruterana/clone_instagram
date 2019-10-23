
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
      profile_image = models.ImageField(upload_to = 'pictures/')
      bio= models.CharField(max_length=30)
      user= models.ForeignKey(User)
      def save_profile(self):
          self.save()
class Image(models.Model):
    image_name= models.CharField(max_length=30)  
    image_caption = models.TextField()
    user= models.ForeignKey(User)
    post = HTMLField()
    image_path = models.ImageField(upload_to = 'pictures/')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    @classmethod
    def search_by_user(cls,search_term):
        username = cls.objects.filter(user__username__icontains=search_term)
        return username
class Comments(models.Model):
    comment = models.CharField(max_length = 250)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    commented_image = models.ForeignKey(Image, on_delete=models.CASCADE, null = True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()
    
    def update_comment(self):
        self.update()

    def __str__(self):
        return self.posted_by
    @classmethod
    def update_caption(cls,id,caption):
        update_image = cls.objects.filter(id = id).update(image_caption = caption)
        return update_image

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id = id).update(user_id = new_user)

    