from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('priority','creator','title','details','date_added','date_due')
    
# Register your models here.
admin.site.register(Task, TaskAdmin)