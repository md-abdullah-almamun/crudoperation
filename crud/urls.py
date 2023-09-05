from django.urls import path
from .views import *

urlpatterns = [
    path('', First, name='first'),
    path('Create/', Create, name='Create'),
    path('Delete/<int:id>/', Delete, name='Delete'),
]
