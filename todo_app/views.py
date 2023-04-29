from django.shortcuts import render, redirect
from todo_app.models import Todo 
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index_view(request):
    data = {
        "todo_list" : Todo.objects.all().order_by('id')
    }
    return render(request, "todo_index.html", data)

def add_todo_view(request):
    if request.method == "POST":
        todo_title = request.POST['todo_title']
        todo_object = Todo.objects.create(title=todo_title)
        return redirect('todo_index') # move to line number 6
    else:
        return HttpResponse("<h1>Access Denied</h1>")
        
def delete_todo_view(request, todo_id):
    if request.method == 'GET':
        todo_object = Todo.objects.get(id=todo_id)
        todo_object.delete()
        return redirect('todo_index') # move to line number 6
    else:
        return HttpResponse("<h1>Access Denied</h1>")
        
    
    
        
    
    
    
