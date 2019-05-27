from django.contrib import admin

from myblog.models import Post
from myblog.models import Category



class CategoryInline(admin.StackedInline):
	model = Category
	

class CategoryAdmin(admin.ModelAdmin):
	exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
	inlines = [CategoryInline,]
	

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
