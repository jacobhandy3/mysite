from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','subtitle','slug','content','visible')
    
# Register your models here.
admin.site.register(Post, PostAdmin)