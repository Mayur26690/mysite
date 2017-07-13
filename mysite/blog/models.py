# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
	STATUS_CHOICE = (
		('draft', 'Draft'),
		('published', 'Published'),
		)
	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250, unique_for_date = 'publish')
	author = models.ForeignKey(User, related_name = 'bolg_posts') #For reverse relationship....(related_name)
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now())
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 10, choices = STATUS_CHOICE, default = 'draft')

	class meta:
		ordering = ('-publish')

	
	def __str__(self):
		return self.title	
