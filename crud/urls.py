from django.urls import path
from .views import *

urlpatterns = [
    path('', First, name='first'),
    path('Create/', Create, name='Create'),
    path('Delete/<int:id>/', Delete, name='Delete'),
    path('see_Profile/<int:id>/', see_Profile, name='see_Profile'),
    path('update_prof/<int:id>/', update_prof, name='update_prof'),
]
