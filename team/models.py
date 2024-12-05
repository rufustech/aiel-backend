from django.db import models

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='team_images/images/')
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        ordering = ['created_at']

    def __str__(self):
        return self.fullname

