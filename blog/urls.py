from django.conf.urls import url

from blog import views
import calendar

urlpatterns = [
    url(r'^archive/(?P<year>\d{4})/(?P<month>' + '|'.join(calendar.month_name).strip('|') + ')/$', views.blogArchive, name='blog_archive'),
    url(r'^categories/([a-zA-Z-]{0,25})/$', views.blogCategories, name='blog_categories'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.blogPosts, name='blog_post'),
    url(r'^$', views.blogRecentPosts, name='blog_recent_posts'),
]
