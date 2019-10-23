from __future__ import unicode_literals

from django.test import TestCase
from .models import Image,Profile

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.image= Profile(profile_image = 'charl1.jpg', bio ='this is my profile')
       
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     
        
        # Testing Save Method of Profile model
    def test_save_method(self):
        self.image.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)         
        
    # Testing  delete method of Profile model     
    def test_delete(self):
        self.image= Profile(profile_image = 'img.jpg', bio ='image')
        self.image.save_profile()
        image = Profile.objects.filter(profile_image = 'img.jpg').first()
        delete = Profile.objects.filter(id = image.id).delete()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.image= Profile(profile = 'img.jpg', bio ='image')
       
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     
        
        # Testing Save Method of Profile model
    def test_save_method(self):
        self.image.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)         
        
    # Testing  delete method of Profile model     
    def test_delete(self):
        self.image= Profile(profile = 'img.jpg', bio ='image')
        self.image.save_profile()
        image = Profile.objects.filter(profile = 'img.jpg').first()
        delete = Profile.objects.filter(id = image.id).delete()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)                 

    def setUp(self):
        self.image= Image(Image = 'img.jpg', bio ='image')
       
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     
        
        # Testing Save Method of Profile model
    def test_save_method(self):
        self.image.save_image()
        images = image.objects.all()
        self.assertTrue(len(images) > 0)         
        
    # Testing  delete method of Image model     
    def test_delete(self):
        self.image= image(image = 'img.jpg')
        self.image.save_image()
        image = Image.objects.filter(Image = 'img.jpg').first()
        delete = Image.objects.filter(id = image.id).delete()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)                   