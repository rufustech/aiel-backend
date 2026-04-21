from django.db import models

class LegalCommentary(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Legal Commentary"
        verbose_name_plural = "Legal Commentaries"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
