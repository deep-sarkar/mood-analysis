from django.urls import path
from . views import MoodAnalyserView

urlpatterns = [
    path('analyse/',MoodAnalyserView.as_view())
]