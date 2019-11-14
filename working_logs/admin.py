from django.contrib import admin

# Register your models here.
from working_logs.models import Project, Opinion


admin.site.register(Project)
admin.site.register(Opinion)