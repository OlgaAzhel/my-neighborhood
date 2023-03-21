from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Report
from .forms import CommentForm
from .serializers import ReportSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')


def reports_index(request):
  # reports = Report.objects.filter(user=request.user)
  reports = Report.objects.all()
  return render(request, 'reports/index.html', {
    'reports': reports
  })


def reports_detail(request, report_id):
  report = Report.objects.get(id=report_id)
  comment_form = CommentForm()
  
  return render(request, 'reports/detail.html', {
    'report': report, 'comment_form': comment_form
  })
  

def add_comment(request, report_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.report_id = report_id
    new_comment.save()
  return redirect('detail', report_id=report_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class ReportCreate(LoginRequiredMixin, CreateView):
  model = Report
  fields = ['title', 'date', 'description', 'location', 'coordX', 'coordY', 'agency']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)


@api_view(['GET'])
def reportsApi(request):
  reports = Report.objects.all()
  data = ReportSerializer(reports, many=True).data
  return Response(data)

class ReportDelete(DeleteView):
  model = Report
  success_url = '/reports'


class ReportUpdate(LoginRequiredMixin, UpdateView):
  model = Report
  fields = ['title', 'date', 'description', 'location', 'coordX', 'coordY', 'agency']
