from django.urls import path
from .views import predictor_view

urlpatterns = [
    path("", predictor_view, name="predictor"),
]