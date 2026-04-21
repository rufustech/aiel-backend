from django.contrib import admin
from .models import Video
from tinymce.widgets import TinyMCE
from django import forms


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    form = VideoForm
    list_display = ('title', 'category', 'speakers', 'featured', 'views', 'year', 'created_at')
    list_filter = ('category', 'featured', 'year', 'created_at')
    search_fields = ('title', 'speakers', 'description', 'tags')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at', 'views')
    fieldsets = (
        ('Video Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Video Source', {
            'fields': ('video_url', 'thumbnail')
        }),
        ('Participants & Content', {
            'fields': ('speakers', 'tags', 'duration_minutes')
        }),
        ('Publishing', {
            'fields': ('year', 'featured')
        }),
        ('Engagement', {
            'fields': ('views',),
            'classes': ('collapse',),
            'description': 'View count for analytics'
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
