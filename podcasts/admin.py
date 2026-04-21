from django.contrib import admin
from .models import Podcast
from tinymce.widgets import TinyMCE
from django import forms


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 15}),
            'transcript': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    form = PodcastForm
    list_display = ('__str__', 'host', 'season', 'episode_number', 'year', 'created_at')
    list_filter = ('season', 'year', 'created_at', 'host')
    search_fields = ('title', 'show_name', 'host', 'guest_speakers', 'description', 'tags')
    ordering = ['-season', '-episode_number', '-created_at']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Episode Information', {
            'fields': ('title', 'show_name', 'season', 'episode_number', 'description')
        }),
        ('Participants', {
            'fields': ('host', 'guest_speakers')
        }),
        ('Audio & Links', {
            'fields': ('audio_file', 'episode_url', 'duration_minutes')
        }),
        ('Content', {
            'fields': ('transcript',),
            'description': 'Full episode transcript for reference and search'
        }),
        ('Media & Organization', {
            'fields': ('thumbnail', 'tags', 'year')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
