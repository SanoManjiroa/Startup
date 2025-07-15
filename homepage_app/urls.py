from django.urls import path, include
from .views import homepage_view
urlpatterns = [
    path('', homepage_view, name='homepage'),
]
