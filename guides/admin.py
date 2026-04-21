from django.contrib import admin
from .models import Guide
from tinymce.widgets import TinyMCE
from django import forms

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = '__all__'
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    form = GuideForm
    list_display = ('title', 'guide_type', 'year', 'created_at')
    list_filter = ('guide_type', 'year', 'created_at')
    search_fields = ('title', 'authors', 'content')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'guide_type', 'year')
        }),
        ('Content', {
            'fields': ('content', 'document')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Authors & Dates', {
            'fields': ('authors', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
