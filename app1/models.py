from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class customuser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    phone_number = models.IntegerField(null=True)
    address = models.TextField(null=True)
    experience = models.TextField(null=True)
    qualification = models.TextField(null=True)
    photo = models.ImageField(upload_to='instructor',null=True)
    date = models.DateField(null=True)
    status = models.IntegerField(default=0)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(null=True,  max_length=255)



class batch(models.Model):
    batch_time = models.TimeField()
    batch_name = models.CharField(null=True, max_length=255)

class equipments(models.Model):
    machine_name = models.CharField(null=True, max_length=255)
    machine_photo = models.ImageField(upload_to='instructor',null=True)

class complaints(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    date = models.CharField(max_length=50)
    reply = models.TextField(max_length=255,null=True)

    def __str__(self):
        return self.subject


class servicemodel(models.Model):
    services = models.CharField(max_length=100)
    image = models.ImageField(upload_to='instructor',null=True)

class attendancemodel(models.Model):
    attendance = models.CharField(max_length=9)
    customer = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.customer


class Bill(models.Model):
    name = models.ForeignKey(customuser,on_delete=models.CASCADE)
    bill_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    paid_on = models.DateField(auto_now=True)
    due_date = models.DateField(null=True)
    status = models.IntegerField(default=0)


class creditcard(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE,null=True)
    card_no = models.CharField(max_length=30)
    card_cvv = models.CharField(max_length=30)
    expiry_date = models.CharField(max_length=200)













