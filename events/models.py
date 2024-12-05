from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name="Event Title")
    location = models.CharField(max_length=200, verbose_name="Event Location")
    start_date = models.DateTimeField(verbose_name="Start Date and Time")
    end_date = models.DateTimeField(verbose_name="End Date and Time")
    speakers = models.TextField() 

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title
