from django.shortcuts import render
from django.http import HttpResponseRedirect
import calendar

from blog.models import Post
from blog.models import Category
from blog.models import BlogRoll
from blog.models import Comment

from blog.forms import CommentForm


def post_shortener(post):
	text_splitted = post.body.split()
	if len(text_splitted) > 250:
		post.body = " ".join(text_splitted[:250])
		post.long_post= True
	return post

def blogPosts(request, post_id):
	post = Post.objects.get(pk=post_id)
	comment = Comment(post=post)
	if request.method == 'POST': # If the form has been submitted...
		form = CommentForm(request.POST, instance=comment) # A form bound to the POST data
		if True: # All validation rules pass
			comm_id = form.save().id
			return HttpResponseRedirect('/blog/posts/%s#comment-%i' % (post_id, comm_id)) # Redirect after POST	
	else:
		form = CommentForm() # An unbound form
	
	context = {'post': post, 'form': form}
	return render(request, 'blog/blog_post.html', context)



def blogCategories(request, ca):
	post_list =  Post.objects.filter(category__name = ca).order_by('-publication_date')
	blog_title = 'Categories'
	context = blogIndex(request, post_list)
	context['blog_title'] = blog_title
	return render(request, 'blog/blog.html', context)


def blogArchive(request, year, month):
	post_list = Post.objects.filter(publication_date__year = year).filter(publication_date__month = calendar.month_name[:].index(month))
	blog_title = 'Archive'
	context = blogIndex(request, post_list)
	context['expand_year'] = int(year)
	context['blog_title'] = blog_title
	return render(request, 'blog/blog.html', context)

def blogRecentPosts(request):
	post_list = Post.objects.order_by('-publication_date')
	blog_title = 'Recent posts'
	context = blogIndex(request, post_list)
	context['blog_title'] = blog_title
	return render(request, 'blog/blog.html', context)

def blogIndex(request, post_list = []):
	map(post_shortener, post_list)
	year_list = [date.year for date in Post.objects.datetimes('publication_date', 'year', order='ASC')]
	category_list = [c for c in Category.objects.order_by('name')]
	posts_ina_year = dict([(year, Post.objects.filter(publication_date__year = year)) for year in year_list])
	year_numpost_dic = dict([(year,len(posts_ina_year[year])) for year in year_list])
	month_numpost_dic = dict([(year, dict([(month, len(filter(lambda x:x.publication_date.strftime('%B')==month, posts_ina_year[year]))) for month in calendar.month_name][1:])) for year in year_list])  
	blogroll_list = BlogRoll.objects.order_by('title')
	ordered_month_list = calendar.month_name[1:]
	context = { 'post_list': post_list, 
				'category_list' : category_list, 
                'year_numpost_dic': year_numpost_dic, 
                'blogroll_list' : blogroll_list,
                'month_numpost_dic': month_numpost_dic,
                'ordered_month_list': ordered_month_list,
				'expand_year': year_list[0],
				}
	return context

