
'''
python manage.py shell
execute the below command inside the shell
exec(open('./my_app2/dbscripts/populate_persons.py').read())
'''

from faker import Faker
from my_app2.models import Person
import random

class PopulatePersons:

    def __init__(self):
        pass

    def run(self):
        fake = Faker()
        LIMIT = 10**3  # 1,000
        for i in range(LIMIT):
            person_obj = Person.objects.create(
                fname=fake.first_name(),
                lname=fake.last_name(),
                age=random.randrange(1, 99),
                gender=random.choice([Person.GENDER.male, Person.GENDER.female, Person.GENDER.others]),
                # gender=random.choice([1, 2 ,3]),
                email=fake.email(),
            )
            print(person_obj)

obj = PopulatePersons()
obj.run()
