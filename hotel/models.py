from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()

class Room(models.Model):

    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    bed_count = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)



class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()



class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)




