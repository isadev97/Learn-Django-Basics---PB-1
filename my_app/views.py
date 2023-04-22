from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    html = """<html>
    <body>
    <h1>Hello world</h1>
    you are hitting the hello world view ! 
    </body>
    </html>
    """ 
    return HttpResponse(html)

def hello_dell(request):
    return render(request, "dell.html")

def test_url(request):
    return render(request, "test.html")
    
    