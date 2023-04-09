
from faker import Faker
from my_app2.models import Person

class PopulatePersons:
    
    def __init__(self):
        pass
    
    def run(self):
        fake = Faker()
        LIMIT = 10**3 # 1,000
        for i in range(LIMIT):
            Person.objects.create(
                fname=,
                lname=,
                age=
                gender=,
                email=
            )
            
    

obj = PopulatePersons()
obj.run()