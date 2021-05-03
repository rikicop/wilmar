from django.db import models

class Post(models.Model):
    
    name =  models.CharField(max_length=200, null=True)
    price = models.FloatField(null= True)
    category = models.CharField(max_length=200,null= True)
    description = models.CharField(max_length=200,null= True,blank=True)
    img = models.FileField(blank=True, null=True)
    #date_created = models.DateTimeField(auto_now_add=True)
    #tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

#Este lo voy a usar para tabla
class Product(models.Model):
    
    name =  models.CharField(max_length=200, null=True)
    price = models.FloatField(null= True)
    category = models.CharField(max_length=200,null= True)
    description = models.CharField(max_length=200,null= True,blank=True)
    img = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.name