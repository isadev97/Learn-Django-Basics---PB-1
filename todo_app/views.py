from django.shortcuts import render
from todo_app.models import Todo 

# Create your views here.
def index_view(request):
    data = {
        "todo_list" : Todo.objects.all().order_by('id')
    }
    return render(request, "todo_index.html", data)
