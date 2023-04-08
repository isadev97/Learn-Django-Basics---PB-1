from django.urls import path
from my_app2.views import hi_world

urlpatterns = [
    path('hi_world', hi_world),
]