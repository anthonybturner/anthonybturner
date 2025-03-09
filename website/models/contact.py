from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    description = models.TextField()
    socal_media_link = models.URLField()

    def __str__(self):
        return self.title
