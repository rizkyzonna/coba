import datetime

#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		#return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
		#was_published_recently.admin_order_field = 'pub_date'
		#was_published_recently.boolean = True
		#was_published_recently.short_description = 'Published Recently?'
		now = timezone.now()
		return now - datetime.timedelta(days=1)<=self.pub_date<=now

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class Judul(models.Model):
	judul_text = models.CharField(max_length=300)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.judul_text
	def recent_published(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1)<=self.pub_date<=now

class Artikel(models.Model):
	judul = models.ForeignKey(Judul)
	isi_artikel = models.CharField(max_length=100000)
	def __str__(self):
		return self.isi_artikel
		
