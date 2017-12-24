from django.db import models
import os
# Create your models here.

def content_album_name(instance, filename):
	return os.path.join(instance.name,filename)

class Info(models.Model):
    name = models.CharField("Name",max_length=128,blank=False)
    email = models.CharField("Email",max_length=128,blank=True)
    mobno = models.CharField("Mob No", max_length=32,blank=True)
    college = models.CharField("College Name",max_length=128,blank=True)
    ans1 = models.FileField(upload_to=content_album_name,blank=False)
    ans2 = models.FileField(upload_to=content_album_name,blank=False)
    ans3 = models.FileField(upload_to=content_album_name,blank=False)
    ans4 = models.FileField(upload_to=content_album_name,blank=False)
    def __str__(self):
        return (self.name)
  #   class Meta:
		# unique = ('name')