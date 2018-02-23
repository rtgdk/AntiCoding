from django.db import models
import os
from django.contrib.auth.models import User
# Create your models here.

def content_album_name(instance, filename):
	return os.path.join(str(instance.teamname1)+str(instance.teamname1),filename)

class Info(models.Model):
    teamname = models.OneToOneField(User)
    teamname1 = models.CharField("Team Member Name 1",max_length=128,blank=False)
    teamname2 = models.CharField("Team Member Name 1", max_length=128, blank=False)
    email1 = models.CharField("Team Member 1 Email",max_length=128,blank=True)
    email2 = models.CharField("Team Member 2 Email", max_length=128, blank=True)
    mobno1 = models.CharField("Mob No 1", max_length=32,blank=True)
    mobno2 = models.CharField("Mob No 2", max_length=32, blank=True)
    #college = models.CharField("College Name",max_length=128,blank=True)
    ans1 = models.FileField(upload_to=content_album_name,blank=True)
    ans2 = models.FileField(upload_to=content_album_name,blank=True)
    ans3 = models.FileField(upload_to=content_album_name,blank=True)
    ans4 = models.FileField(upload_to=content_album_name,blank=True)
    ans5 = models.FileField(upload_to=content_album_name,blank=True)
    ans1score = models.IntegerField("Ans 1 score",default=0)
    ans2score = models.IntegerField("Ans 2 score", default=0)
    ans3score = models.IntegerField("Ans 3 score", default=0)
    ans4score = models.IntegerField("Ans 4 score", default=0)
    ans5score = models.IntegerField("Ans 5 score", default=0)
    round1score = models.IntegerField("Round 1 score",default=0)
    round2score = models.IntegerField("Round 2 score", default=0)
    endround2 = models.IntegerField("Round 2 end",default=0)
    def __str__(self):
        return (self.teamname1+" "+self.teamname2)

class ForAdmin(models.Model):
	name = models.CharField("Name",max_length=10,blank=False)
	round1 = models.IntegerField("Round 1 begin",default=0)
	round2 = models.IntegerField("Round 2 begin", default=0)
	round3 = models.IntegerField("Round 2 ends", default=0)
  #   class Meta:
		# unique = ('name')