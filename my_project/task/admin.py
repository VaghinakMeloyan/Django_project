from django.contrib import admin
from .models import Task
from .models import Target

admin.site.register(Task)
admin.site.register(Target)
