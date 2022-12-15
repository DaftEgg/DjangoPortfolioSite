from django.db import models

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    project_link = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return self.project_title