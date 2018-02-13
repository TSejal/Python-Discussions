from django.contrib import admin
from discussion.models import *

# Register your models here.

class DiscussionsAdmin(admin.ModelAdmin):
    fieldsets = (
           ('Discussion data', {'fields': ('title', 'added_by','image', 'discussion_type','text')}),
           ('Date', {'fields': ('created_date','modified_date')}),
	        ('Permission', {'fields': ('is_published', )}),
    	)


class CommentsAdmin(admin.ModelAdmin):
    fieldsets = (
           ('Discussion data', {'fields': ('discussion', 'added_by','text')}),
           ('Date', {'fields': ('created_date','modified_date')}),
    	)


admin.site.register(Discussion,DiscussionsAdmin)
admin.site.register(Comment,CommentsAdmin)