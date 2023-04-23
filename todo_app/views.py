from django.shortcuts import render, redirect
from todo_app.models import Todo 

# Create your views here.
def index_view(request):
    data = {
        "todo_list" : Todo.objects.all().order_by('id')
    }
    return render(request, "todo_index.html", data)

def add_todo_view(request):
    todo_title = request.POST['todo_title']
    Todo.objects.create(title=todo_title)
    return redirect('todo_index')
    
    
