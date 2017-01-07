from django.contrib import admin

from .models import Project
# Register your models here.
class projectAdmin(admin.ModelAdmin):
	list_display = ('project_title',)
	search_fields = ['project_title']

admin.site.register(Project, projectAdmin)
