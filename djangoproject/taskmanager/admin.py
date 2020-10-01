from django.contrib import admin
from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'title', 'description', 'date', 'status', 'end_date',)
    list_display_links = ('user', 'title',)
    search_fields = ('user', 'id', 'title', 'description', 'date', 'status', 'end_date',)
    list_editable = ('status',)


admin.site.register(Task, TaskAdmin)
