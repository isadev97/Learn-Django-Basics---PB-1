from django.db import models

# Create your models here.
class Person(models.Model):
    
    # id = models.BigAutoField(primary_key=True)
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    ]
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(default=0, null=True)
    email = models.EmailField()
    
    # class Meta:
    #     db_table="person"
        
        