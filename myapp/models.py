from django.db import models

class User(models.Model):
    age=models.IntegerField()
    uname=models.CharField(max_length=50)
    upassword=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    class meta:
        db_table='user'
class Expence(models.Model):
    time=models.TimeField() 
    date=models.DateField() 
    remark=models.CharField(max_length=100)
    amount=models.FloatField() 
    category=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class meta:
        db_table='expence'
    
class Income(models.Model):
    time=models.TimeField() 
    date=models.DateField() 
    remark=models.CharField(max_length=100)
    amount=models.FloatField() 
    category=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class meta:
        db_table='income'
    
