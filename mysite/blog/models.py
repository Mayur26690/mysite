# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class PublishedManager(models.Manager):
	"""docstring for PublishedManager"""
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status = 'published')

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

	objects = models.Manager()
	published = PublishedManager()

	class meta:
		ordering = ('-publish')

	def get_absolute_url(self):
		return reverse('blog:post_details', args = [self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'),self.slug])

	def __str__(self):
		return self.title	


		