from django.db import models

class Subscription(models.Model):
    email_address = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.email_address
