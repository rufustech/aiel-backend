from django.db import models
from tinymce.models import HTMLField


class Video(models.Model):
    """Video resource"""
    CATEGORY_CHOICES = [
        ('educational', 'Educational'),
        ('interview', 'Interview'),
        ('webinar', 'Webinar'),
        ('keynote', 'Keynote'),
        ('documentary', 'Documentary'),
        ('advocacy', 'Advocacy & Action'),
        ('panel', 'Panel Discussion'),
        ('tutorial', 'Tutorial'),
        ('announcement', 'Announcement'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Video Title")
    description = HTMLField(verbose_name="Video Description & Transcript")
    
    # Video hosting
    video_url = models.URLField(verbose_name="Video URL (YouTube, Vimeo, etc.)")
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', verbose_name="Custom Thumbnail")
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='educational')
    speakers = models.CharField(max_length=500, verbose_name="Speakers/Presenters (comma-separated)")
    
    # Metadata
    duration_minutes = models.PositiveIntegerField(verbose_name="Duration (minutes)", blank=True, null=True)
    tags = models.CharField(max_length=500, verbose_name="Tags (comma-separated)", blank=True)
    year = models.PositiveIntegerField(verbose_name="Year")
    featured = models.BooleanField(default=False, verbose_name="Featured Video")
    
    # Engagement
    views = models.PositiveIntegerField(default=0, verbose_name="View Count")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
