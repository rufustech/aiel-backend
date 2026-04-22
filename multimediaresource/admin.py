from django.contrib import admin
from .models import MultimediaResource

class MultimediaResourceAdmin(admin.ModelAdmin):
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

admin.site.register(MultimediaResource, MultimediaResourceAdmin)
