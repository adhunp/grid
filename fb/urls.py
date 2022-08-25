from django.urls import path
from .import views

urlpatterns=[
    path('',views.grid),
    path('adhun',views.adhun),
]