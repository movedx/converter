from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('result/<int:file_id>/', views.result, name='result'),
]
