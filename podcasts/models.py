from django.db import models
from tinymce.models import HTMLField


class Podcast(models.Model):
    """Podcast episode resource"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Episode Title")
    show_name = models.CharField(max_length=255, verbose_name="Podcast Show Name", default="AIEL Podcast")
    description = HTMLField(verbose_name="Episode Description & Show Notes")
    episode_number = models.PositiveIntegerField(verbose_name="Episode Number", blank=True, null=True)
    season = models.PositiveIntegerField(verbose_name="Season", default=1)
    host = models.CharField(max_length=255, verbose_name="Host/Narrator")
    guest_speakers = models.TextField(verbose_name="Guest Speakers (comma-separated)", blank=True)
    
    # Audio/Link options
    audio_file = models.FileField(
        upload_to='podcasts/audio/',
        verbose_name="Audio File (MP3/WAV)",
        blank=True,
        null=True
    )
    episode_url = models.URLField(
        verbose_name="Episode URL (Spotify, Apple Podcasts, etc.)",
        blank=True
    )
    
    transcript = HTMLField(verbose_name="Episode Transcript", blank=True)
    duration_minutes = models.PositiveIntegerField(verbose_name="Duration (minutes)", blank=True, null=True)
    thumbnail = models.ImageField(upload_to='podcasts/thumbnails/', verbose_name="Album Art/Thumbnail")
    tags = models.CharField(max_length=500, verbose_name="Tags (comma-separated)", blank=True)
    year = models.PositiveIntegerField(verbose_name="Year")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Podcast Episode"
        verbose_name_plural = "Podcast Episodes"
        ordering = ['-season', '-episode_number', '-created_at']

    def __str__(self):
        if self.episode_number:
            return f"S{self.season}E{self.episode_number}: {self.title}"
        return self.title
