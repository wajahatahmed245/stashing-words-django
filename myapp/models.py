from django.db import connection
from django.db import models

# Create your models here.

class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    contact    = models.IntegerField()  
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()  


class Employee(models.Model):  
    eid      = models.CharField(max_length=20)  
    ename    = models.CharField(max_length=100)  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"       





def mysql():
    with connection.cursor() as cursor:
        cursor.execute("select * from company ")
        row = cursor.fetchall()

    return row