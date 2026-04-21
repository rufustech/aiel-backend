from django.db import models
from tinymce.models import HTMLField


class PhotoGallery(models.Model):
    """Collection/Series of photos"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Gallery Title")
    description = HTMLField(verbose_name="Gallery Description")
    year = models.PositiveIntegerField(verbose_name="Year")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Photo Gallery"
        verbose_name_plural = "Photo Galleries"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Individual photo resource"""
    CATEGORY_CHOICES = [
        ('event', 'Event Coverage'),
        ('landscape', 'Landscape'),
        ('portrait', 'Portrait'),
        ('documentary', 'Documentary'),
        ('advocacy', 'Advocacy & Action'),
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('community', 'Community'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Photo Title")
    caption = HTMLField(verbose_name="Photo Caption & Description")
    photographer = models.CharField(max_length=255, verbose_name="Photographer")
    location = models.CharField(max_length=255, verbose_name="Location", blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='documentary')
    gallery = models.ForeignKey(PhotoGallery, on_delete=models.SET_NULL, null=True, blank=True, related_name='photos')
    image = models.ImageField(upload_to='photos/', verbose_name="Photo Image")
    tags = models.CharField(max_length=500, verbose_name="Tags (comma-separated)", blank=True)
    year = models.PositiveIntegerField(verbose_name="Year")
    featured = models.BooleanField(default=False, verbose_name="Featured Photo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
