from django.urls import path
from .views import ActivityView

urlpatterns = [
    path('activity/', ActivityView.as_view()),
    path('activity/<int:pk>/', ActivityView.as_view())
]