from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    main_content = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.title