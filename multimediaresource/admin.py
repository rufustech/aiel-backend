from django.contrib import admin
from .models import MultimediaResource

admin.site.register(MultimediaResource)
from django.contrib import admin
from .models import MultimediaResource
from tinymce.widgets import TinyMCE
from django import forms

class MultimediaResourceForm(forms.ModelForm):
    class Meta:
        model = MultimediaResource
        fields = '__all__'
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

class MultimediaResourceAdmin(admin.ModelAdmin):
    form = MultimediaResourceForm
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

admin.site.register(MultimediaResource, MultimediaResourceAdmin)
