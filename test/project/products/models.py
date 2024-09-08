from django.db import models
from datetime import datetime

# Create your models here.


class Product(models.Model):

    catecoryChoices=[
        ('phone',  'phone'),
        ('computer', 'computer'),
        ('laptop', 'laptop'),
        ('tablet', 'tablet'),
    ]



    name=  models.CharField(max_length=50, default='mobile phone' , verbose_name='title') #verbose_name is to rename it in the admin panel.
    content = models.TextField(null=True ,  blank=True) #blank means not required ,  null means defult value is empty
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=10.0)
    category = models.CharField(  max_length=50,null=True ,  blank=True, choices=  catecoryChoices)
    image = models.ImageField(upload_to='pics/%y/%m/%d' , default='pics/24/09/08/1700305225689.jpeg')
    active =  models.BooleanField(default=True)

    def  __str__(self):
        return self.name
    # this self is refered to the class. 

    class  Meta:
        verbose_name = 'Product'
    # this is the name of the database table name in the admin  panel. 
        ordering = ['name']  # this is to order the product when show it. 


class Time(  models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    dateTime=  models.DateTimeField(default=datetime.now, null=True)
    