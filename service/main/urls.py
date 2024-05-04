from django.urls import path

from main import views


urlpatterns = [
    path('', views.get_index, name='index')
]