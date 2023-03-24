from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


AGENCIES = (
    ('P', 'Police'),
    ('T', 'Transportation'),
    ('F', 'Fire'),
    ('H', 'Health'),
    ('S', 'Sanitation'),
    ('U', 'Utilities'),
    ('O', 'Other'),
)
STATUS_CHOICE = (
    ('P', 'Pending'),
    ('S', 'Solved'),
)

class Report(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=250)
    date = models.DateField('Date Filed')
    location = models.CharField(
        max_length=300, default="", null=True, blank=True)
    coordX = models.FloatField(default=0, null=True, blank=True)
    coordY = models.FloatField(default=0, null=True, blank=True)
    agency = models.CharField(
        max_length=1,
            choices=AGENCIES,
            default=AGENCIES[0][0])
    status = models.CharField(
        max_length=1, 
            choices=STATUS_CHOICE,
            default=STATUS_CHOICE[0][0]
            
        )
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'report_id': self.id})
    
    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Date', default=date.today)
    content = models.TextField('Leave a Comment', max_length=250)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} ({self.id})'

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for report_id: {self.report_id} @{self.url}"