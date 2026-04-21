from django.contrib import admin
from .models import Photo, PhotoGallery
from tinymce.widgets import TinyMCE
from django import forms


class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 15}),
        }


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    form = PhotoGalleryForm
    list_display = ('title', 'year', 'created_at')
    list_filter = ('year', 'created_at')
    search_fields = ('title', 'description')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Gallery Information', {
            'fields': ('title', 'description', 'year')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {
            'caption': TinyMCE(attrs={'cols': 80, 'rows': 15}),
        }


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm
    list_display = ('title', 'photographer', 'category', 'gallery', 'featured', 'year', 'created_at')
    list_filter = ('category', 'gallery', 'featured', 'year', 'created_at')
    search_fields = ('title', 'photographer', 'location', 'tags', 'caption')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Photo Information', {
            'fields': ('title', 'caption', 'photographer', 'location')
        }),
        ('Organization', {
            'fields': ('gallery', 'category', 'tags')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Publishing', {
            'fields': ('year', 'featured')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
