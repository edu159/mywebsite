from django.contrib import admin
from blog.models import Post 
from blog.models import Category
from blog.models import BlogRoll
from blog.models import Comment
from django.conf import settings

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'publication_date','published', 'body', 'category']
	list_display = ('title', 'publication_date', 'getCategoriesStr', 'published')
	filter_horizontal = ('category',)
	class Media:
		js = ('js/tiny_mce/tiny_mce.js','js/tiny_mce/textarea.js')


class CategoryAdmin(admin.ModelAdmin):
	fields = ['name']

class BlogRollAdmin(admin.ModelAdmin):
	list_display = ('title', 'link')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'publication_date', 'id')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogRoll, BlogRollAdmin)
admin.site.register(Comment, CommentAdmin)
