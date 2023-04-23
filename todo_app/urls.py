from django.urls import path
from todo_app.views import index_view

urlpatterns = [
    path('index', index_view),
    # path('hello-world', hello_world), 
    # path('person-info/<str:encrypted_id>', person_info)
]