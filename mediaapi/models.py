from django.db import models

class Mediaapi(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='gallery_images/images/')
    media_name = models.CharField(max_length=255)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"
        ordering = ['created_at']
    
    def __str__(self):
        return self.media_name
