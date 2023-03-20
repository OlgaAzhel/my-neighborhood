from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('reports/create/', views.ReportCreate.as_view(), name='report_create'),
]   

