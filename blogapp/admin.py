from django.contrib import admin
from blogapp.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('title', 'counted_views' , 'created_date', 'updated_date', 'status')

admin.site.register(Post, PostAdmin)