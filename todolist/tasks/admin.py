from django.contrib import admin
from tasks.models import Tasks, Categories


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_id", "title", "user", "due_date")


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "name", "user")
