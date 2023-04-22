from django.urls import path
from my_app2.views import hi_world, hello_world, person_info

urlpatterns = [
    path('hi_world', hi_world),
    path('hello-world', hello_world), 
    path('person-info/<str:encrypted_id>', person_info)
]