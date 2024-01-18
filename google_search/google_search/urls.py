from django.contrib import admin
from django.urls import path
from google_search_app import views

urlpatterns = [
    path('', views.home),
    path('result', views.result),
    path('download', views.download),
    path('successful_download', views.successful_download)
]
