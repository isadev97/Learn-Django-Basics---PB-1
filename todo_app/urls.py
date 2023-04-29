from django.urls import path
from todo_app.views import index_view, add_todo_view, delete_todo_view

urlpatterns = [
    path('index', index_view, name='todo_index'),
    path('add-todo/', add_todo_view, name='add_todo'), 
    path('delete-todo/<int:todo_id>/', delete_todo_view, name='delete_todo'), 
    
]