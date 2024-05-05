from django.db import models

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='attraction_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
