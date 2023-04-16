"""
URL configuration for sphinxdemo project.
"""
from django.urls import (
    include,
    path,
)


urlpatterns = [
    path('', include("hello.urls")),
]
