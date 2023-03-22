from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reports/', views.reports_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('reports/create/', views.ReportCreate.as_view(), name='report_create'),
    path('reports/<int:pk>/delete/', views.ReportDelete.as_view(), name='reports_delete'),
    path('reports/<int:report_id>/', views.reports_detail, name='detail'),
    path('reports/<int:report_id>/add_comment/', views.add_comment, name='add_comment'),
    path('reports/<int:report_id>/add_photo/', views.add_photo, name='add_photo'),
    path('reportsApi/', views.reportsApi, name='reportsApi'),
    path('photosApi/', views.photosApi, name='photosApi'),
    path('reports/<int:pk>/update/', views.ReportUpdate.as_view(), name='report_update'),
    path('reports/<int:report_id>/change_status/', views.change_status, name='change_status'),
]   

