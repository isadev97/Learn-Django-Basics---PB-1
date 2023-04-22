from django.shortcuts import render

# Create your views here.
def hi_world():
    pass


def hello_world_replica():
    return "hello world"

def hello_world(request):
    return render(request, "hello_world.html")
