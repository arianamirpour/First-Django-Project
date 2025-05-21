from django.contrib import admin
from django.urls import path
from firstapp.views import *

app_name = 'firstapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
] 