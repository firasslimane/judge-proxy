from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contest(models.Model):
	title = models.CharField(max_length=128)
	start_time = models.DateTimeField('Contest Start Time')
	lock_time = models.DateTimeField('Board Lock Time')
	end_time = models.DateTimeField('Contest End Time')

	def __unicode__(self):
		return self.title

	class Admin:
		pass

class Onlinejudge(models.Model):
	title = models.CharField(max_length=8)
	
	def __unicode__(self):
		return self.title

class Problem(models.Model):
	title = models.CharField(max_length=128)
	url = models.CharField(max_length=256)
	srcsite = models.ForeignKey(Onlinejudge)
	srcpid  = models.IntegerField()
	contest = models.ForeignKey(Contest)
	
	def __unicode__(self):
		return "%d-%s"%(self.id,self.title)

class Solution(models.Model):
	LANG_CHOICES=(
		(u'C',u'C'),
		(u'X',u'CPP'),
		(u'J',u'JAVA'),
		(u'P',u'PASCAL'),
	)
	STATUS_CHOICES=(
		(u'Y',u'Yes'),
		(u'N',u'No'),
		(u'J',u'Judging'),
		(u'P',u'Pending'),
	)
	problem = models.ForeignKey(Problem)
	user = models.ForeignKey(User)
	submittime = models.DateTimeField('Submit time')
	subipaddr = models.CharField(max_length=16)
	language = models.CharField(max_length=2,choices=LANG_CHOICES)
	status = models.CharField(max_length=2,choices=STATUS_CHOICES)
	reason = models.CharField(max_length=16)
	source = models.TextField()

	
