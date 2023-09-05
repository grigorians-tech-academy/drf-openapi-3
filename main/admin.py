from django.contrib import admin

from .models import LogItem, Project, Task

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "owner"]
    list_filter = ["owner"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_at", "completed"]
    search_fields = ["title", "description"]


@admin.register(LogItem)
class LogItemAdmin(admin.ModelAdmin):
    list_display = ["comment", "created_at"]
