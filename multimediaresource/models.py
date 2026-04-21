from django.db import models

class MultimediaResource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    resource_url = models.URLField()
    resource_type = models.CharField(max_length=100, choices=[
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
        ('image', 'Image'),
        ('other', 'Other'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Multimedia Resource"
        verbose_name_plural = "Multimedia Resources"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
