# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	# paginate_by = 4
	template_name = 'blog/post/list.html'
# def post_list(req):
# 	posts = Post.objects.all()
# 	object_list = Post.objects.all()
# 	paginator = Paginator(object_list,5) # 3 post in each page
# 	page = req.GET.get('page') #GET current page number
# 	try:
# 		posts = paginator.page(page)
# 	except PageNotAnInteger:# If page is not an integer deliver the first page
# 		posts = paginator.page(1)
# 	except EmptyPage:# If page is out of range deliver last page of results
# 		posts = paginator.page(paginator.num_pages)
# 	print posts
# 	return render(req, 'blog/post/list.html',{'posts':posts, 'page':page})

def post_details(req, year,month,day,post):
	post1 = get_object_or_404(Post, slug = post,status = 'published',
		publish__year = year, 
		publish__month = month, 
		publish__day = day)
	return render(req, 'blog/post/detail.html',{'post':post1})