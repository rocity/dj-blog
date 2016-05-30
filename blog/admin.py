from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Tag

class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    list_display = ('title', 'owner', 'status', 'created')
    list_filter = ('status',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
admin.site.register(Tag)
