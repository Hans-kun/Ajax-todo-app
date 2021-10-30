from django.contrib import admin
from .models import TodoList

# Register your models here.
admin.site.register(TodoList)

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

