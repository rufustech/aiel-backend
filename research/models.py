from django.db import models
from tinymce.models import HTMLField

class Research(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Research Title")
    document = models.FileField(upload_to='research_docs/', verbose_name="Document (PDF)", null=True, blank=True)
    content = HTMLField()
    year = models.PositiveIntegerField(verbose_name="Year of Publication")
    authors = models.TextField(verbose_name="Authors")
    footnote = models.TextField(verbose_name="Footnote")
    image = models.ImageField(upload_to='research_images/', verbose_name="Image", null=True, blank=True)

    class Meta:
        verbose_name = "Research"
        verbose_name_plural = "Research Studies"

    def __str__(self):
        return self.title
