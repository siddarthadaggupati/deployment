from django.db import models

class CalendarEvent(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    hyperlink = models.URLField()

