from __future__ import unicode_literals

from django.test import TestCase
from .models import Image,Profile

# Create your tests here.

class ProfileTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.charlene= Profile(profile_image = 'cat.jpeg', bio ='this is my profile')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.charlene,Profile))

    def test_save_profile(self):
        self.user = Profile(profile_image='charlene.jpg',bio='media')
        self.user.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    def test_update_profile(self):
        self.media = Profile(profile_image='charlene.jpg',bio='media')
        self.media.save_profile()
        charlene =Profile.objects.filter(bio='media').first()
        update= Profile.objects.filter(id=charlene.id).update(bio='media')
        updated = Profile.objects.filter(bio = 'media').first()
        self.assertNotEqual(charlene.biography , updated.bio)

    def test_delete_profile(self):
        self.charlene = Profile(profile_image='cat.jepg',bio='this is my prrofile')
        self.chaarlene.save_profile()
        cat = Profile.objects.filter(biography='Awesome').first()
        cat= Profile.objects.filter(id =nature.id).delete()
        cat =Profile.objects.all()
        


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.cat= Image(image = 'cat.jpeg', name ='cat')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cat,Image))

    def test_save_image(self):
        self.cat2 = Image(image='cat2.jpeg',name='cat2')
        self.cat2.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    
    # def test_update_image(self):
    #     self.cat3 = Image(image='cat3.jepg',name='cat3')
    #     self.cat3.save_image()
    #     cat3 =Image.objects.filter(name='cat3').first()
    #     update= Image.objects.filter(id=cat3.id).update(name='cat3')
    #     updated = Image.objects.filter(name = 'cat3').first()
    #     self.assertNotEqual(cat3.name , updated.name)

    def test_delete_image(self):
        self.forest = Image(image='cat4.jepg',name='cat')
        self.forest.save_image()
        cat4 = Image.objects.filter(name='cat4').first()
        tree = Image.objects.filter(id =cat4.id).delete()
        trees =Image.objects.all()
        

