from django.db import models
from tinymce.models import HTMLField

class ResearchHighlight(models.Model):
    title = models.CharField(max_length=255, verbose_name="Research Highlight Title")
    content = HTMLField()
    year = models.PositiveIntegerField(verbose_name="Year of Publication")
    authors = models.TextField(verbose_name="Authors")
    image = models.ImageField(upload_to='research_highlight_images/', verbose_name="Image", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Research Highlight"
        verbose_name_plural = "Research Highlights"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
