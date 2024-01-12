from django.db import models
from django.contrib.auth.models import User


class services_cateogaries(models.Model):
    cateogary = models.CharField(max_length=200,default="NIL")
    image = models.ImageField(upload_to="categaries",blank=True)

    def __str__(self):
        return self.cateogary    



class services(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Services")
    price = models.IntegerField()
    cate = models.ForeignKey(services_cateogaries,default=1, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name 


class Bookins(models.Model):
    Client_Name = models.CharField(max_length=50,default='NIL')
    Address = models.CharField(max_length=1000,default="nil")
    Book = models.ForeignKey(services,on_delete=models.CASCADE , default=1)
    price = models.IntegerField(default=0)
    client_number = models.IntegerField(default=0)
    cateogary = models.ForeignKey(services_cateogaries, on_delete=models.CASCADE,default=1)
    checked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.Client_Name} Wants to Book for {self.Book} pricing {self.price} rs"



class Appointment(models.Model):
    Name = models.CharField(max_length=200)
    Ph = models.CharField(max_length=10)
    Email = models.CharField(max_length=200, default="Not Assigned By User")
    def __str__(self):
        if self.Email == "Not Assigned By User":
            return f"{self.Name} : {self.Ph} - tried to contact us"
        else:
            return f"{self.Name} : {self.Ph} - is Looking for an Appointment"


class review(models.Model):
    Name = models.CharField(max_length=100)
    review = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Name} : {self.created_at}"


class IP(models.Model):
    Ip = models.CharField(max_length=100)

    def __str__(self):
        return f"a guy with ip {self.Ip} tried uneven methods on website" 


class gall(models.Model):
    image = models.ImageField( upload_to="Gallery")
