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
