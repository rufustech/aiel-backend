from django.db import models
from tinymce.models import HTMLField

class CaseStudy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Case Study Title")
    content = HTMLField()
    year = models.PositiveIntegerField(verbose_name="Year of Publication")
    authors = models.TextField(verbose_name="Authors")
    image = models.ImageField(upload_to='case_study_images/', verbose_name="Image", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
