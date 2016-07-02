from django.contrib import admin
from .models import Category, Task, Settings

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Settings)

# Register your models here.
