from django.contrib import admin
from .models import Newsletter
from tinymce.widgets import TinyMCE
from django.db import models

class NewsletterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = ('title', 'year', 'created_at')
    list_filter = ('year', 'created_at')
    search_fields = ('title', 'authors', 'content')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'year', 'authors')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Newsletter, NewsletterAdmin)
