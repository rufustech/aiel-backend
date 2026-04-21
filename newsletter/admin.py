from django.contrib import admin
from .models import Newsletter
from tinymce.widgets import TinyMCE
from django.db import models

class NewsletterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Newsletter, NewsletterAdmin)
