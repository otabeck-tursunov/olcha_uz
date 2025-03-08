from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('me/', AccountRetrieveUpdateDestroyAPIView.as_view()),
]
