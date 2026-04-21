from django.db import models

class ResearchHighlight(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='research_images/', null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Research Highlight"
        verbose_name_plural = "Research Highlights"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
