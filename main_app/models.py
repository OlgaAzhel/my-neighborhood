from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


AGENCIES = (
    ('P', 'Police'),
    ('T', 'Transportation'),
    ('F', 'Fire'),
    ('H', 'Health'),
    ('S', 'Sanitation'),
    ('U', 'Utilities'),
    ('O', 'Other'),
)

class Report(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('Date Filed')
    description = models.TextField(max_length=250)
    location = models.CharField(
        max_length=300, default="", null=True, blank=True)
    coordX = models.FloatField(default=0, null=True, blank=True)
    coordY = models.FloatField(default=0, null=True, blank=True)
    agency = models.CharField(
        max_length=1,
            choices=AGENCIES,
            default=AGENCIES[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('index')


    