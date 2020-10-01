from django.db import models

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption
