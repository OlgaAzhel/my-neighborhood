from django.forms import ModelForm
from .models import Comment
from .models import Report

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']

class ReportStatus(ModelForm):
  class Meta:
    model = Report
    fields = [ 'status']
    exclude=['title', 'date', 'description', 'location', 'coordX', 'coordY', 'agency']