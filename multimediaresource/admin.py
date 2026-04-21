from django.contrib import admin
from .models import MultimediaResource

class MultimediaResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'created_at')
    list_filter = ('resource_type', 'created_at')
    search_fields = ('title', 'description')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'resource_type')
        }),
        ('Content', {
            'fields': ('description', 'resource_url')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(MultimediaResource, MultimediaResourceAdmin)
