from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	project_title = models.CharField(max_length=200)
	project_description = models.CharField(max_length=1000)
	project_date = models.DateTimeField('Project Date')
	project_githubLink = models.CharField(max_length=200)
