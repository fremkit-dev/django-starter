from django.urls import path
from mysite.views import hello

urlpatterns = [
    path('', hello),
]
