from django.db import models
from tinymce.models import HTMLField

class Brief(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Brief Title")
    document = models.FileField(upload_to='brief_docs/', verbose_name="Document (PDF)", null=True, blank=True)
    content = HTMLField()
    year = models.PositiveIntegerField(verbose_name="Year of Publication")
    authors = models.TextField(verbose_name="Authors")
    image = models.ImageField(upload_to='brief_images/', verbose_name="Image", null=True, blank=True)
    footnote = models.TextField(verbose_name="Footnote")

    class Meta:
        verbose_name = "Brief"
        verbose_name_plural = "Briefs"

    def __str__(self):
        return self.title
