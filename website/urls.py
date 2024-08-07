from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('', views.upload_file, name='home'),
    path('result/<media_file_ids>/', views.result, name='result'),
    path('download/<int:media_file_id>/', views.download_file, name='download_file'),
    path('test', views.test_response, name='test'),
]
