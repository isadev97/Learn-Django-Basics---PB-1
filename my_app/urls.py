from django.urls import path
from my_app.views import hello_world

urlpatterns = [
    # domain_name/app_name/route
    # localhost/my-app/hello
    path('hello', hello_world),
]