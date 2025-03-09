from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    technologies_used = models.TextField()
    link = models.URLField()
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title
