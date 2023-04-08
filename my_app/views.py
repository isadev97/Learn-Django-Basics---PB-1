from django.http import HttpResponse

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
    
    