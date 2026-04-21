from django.contrib import admin
from .models import ResearchHighlight
from tinymce.widgets import TinyMCE
from django.db import models

class ResearchHighlightAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(ResearchHighlight, ResearchHighlightAdmin)
from django.contrib import admin
from .models import ResearchHighlight
from tinymce.widgets import TinyMCE
from django import forms

class ResearchHighlightForm(forms.ModelForm):
    class Meta:
        model = ResearchHighlight
        fields = '__all__'
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

class ResearchHighlightAdmin(admin.ModelAdmin):
    form = ResearchHighlightForm
    list_display = ('title', 'year', 'authors', 'created_at')
    list_filter = ('year', 'created_at')
    search_fields = ('title', 'authors', 'content')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'authors', 'year')
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

admin.site.register(ResearchHighlight, ResearchHighlightAdmin)
