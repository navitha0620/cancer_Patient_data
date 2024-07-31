from django.db import models

# Create your models here.


class Register(models.Model):
    email=models.EmailField(primary_key=True,max_length=50)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    hospitalname=models.CharField(max_length=100)
    branchaddress=models.CharField(max_length=50)
   # firstname=models.CharField(max_length=100)
    subject=models.CharField(max_length=150)
    design=models.CharField(max_length=15,default="user")
    #department=models.CharField(max_length=50)
    #doctor=models.CharField(max_length=100)
    def __str__(self):
        #return self.email+","+self.
        return self.email