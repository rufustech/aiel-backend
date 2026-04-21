from django.db import models
from tinymce.models import HTMLField


class Guide(models.Model):
    GUIDE_TYPE_CHOICES = [
        ('guide', 'Guide'),
        ('toolkit', 'Toolkit'),
        ('template', 'Template'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Guide/Toolkit Title")
    content = HTMLField()
    guide_type = models.CharField(max_length=20, choices=GUIDE_TYPE_CHOICES, default='guide')
    document = models.FileField(upload_to='guides_docs/', verbose_name="Document (PDF)", null=True, blank=True)
    image = models.ImageField(upload_to='guides_images/', verbose_name="Image", null=True, blank=True)
    year = models.PositiveIntegerField(verbose_name="Year of Publication")
    authors = models.TextField(verbose_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Guide & Toolkit"
        verbose_name_plural = "Guides & Toolkits"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
