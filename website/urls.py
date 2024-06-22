from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('', views.upload_file, name='home'),
    path('result/<int:media_file_id>/', views.result, name='result'),
]
