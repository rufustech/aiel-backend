from django.contrib import admin
from .models import LegalCommentary
from tinymce.widgets import TinyMCE
from django import forms

class LegalCommentaryForm(forms.ModelForm):
    class Meta:
        model = LegalCommentary
        fields = '__all__'
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

class LegalCommentaryAdmin(admin.ModelAdmin):
    form = LegalCommentaryForm
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

admin.site.register(LegalCommentary, LegalCommentaryAdmin)
