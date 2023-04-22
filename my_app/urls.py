from django.urls import path
from my_app.views import hello_world, hello_dell, test_url

urlpatterns = [
    # domain_name/app_name/route
    # localhost/my-app/hello
    path('hello', hello_world),
    path('hello-dell', hello_dell),
    path('test-url', test_url)
]