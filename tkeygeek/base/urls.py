from django.urls import path

from tkeygeek.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
