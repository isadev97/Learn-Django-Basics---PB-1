from django.shortcuts import render
from my_app2.models import Person
from hashids import Hashids
from django.conf import settings

# Create your views here.
def hi_world():
    pass


def hello_world_replica():
    return "hello world"

def hello_world(request):
    show_oldest_person = False
    my_data = {
        "name" : "Ishjot",
        "tech_stack" : "Python",
        "role" : "Software developer",
        "person_list": Person.objects.filter(id__lte=10),
        "oldest_person_list" :  Person.objects.all().order_by('-age')[:10] if show_oldest_person else []
    }
    return render(request, "hello_world.html", my_data)

def person_info(request, encrypted_id):
    hashids = Hashids(salt=settings.PRIVATE_KEY)
    decrypted_id = hashids.decode(encrypted_id)[0]
    print("decrypted id", decrypted_id)
    person_object = Person.objects.get(id=decrypted_id)
    my_data = {
        "Fname" : person_object.fname,
        "Lname" : person_object.lname,
        "email" : person_object.email
    }
    return render(request, "person_info.html", my_data)



