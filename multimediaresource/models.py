from django.db import models
from tinymce.models import HTMLField

class MultimediaResource(models.Model):
    title = models.CharField(max_length=255, verbose_name="Multimedia Resource Title")
    content = HTMLField()
    year = models.PositiveIntegerField(verbose_name="Year of Publication")
    authors = models.TextField(verbose_name="Authors")
    image = models.ImageField(upload_to='multimedia_resource_images/', verbose_name="Image", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Multimedia Resource"
        verbose_name_plural = "Multimedia Resources"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
