# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(req):
	posts = Post.published.all()
	return render(req, 'blog/post/list.html',{'posts':posts})

def post_details(req, year,month,day,post):
	posst = get_object_or_404(Post, slug = post,status = 'published',
		publish__year = year, 
		publish__month = month, 
		publish__day = day)
	return render(req, 'blog/post/detail.html',{'post':post})