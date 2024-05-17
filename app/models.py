from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 300)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='imags/')
    rating = models.FloatField()
    discount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.name
    @property
    def discount_price(self):
        if self.discount > 0:
         return self.price * (1 - self.discount / 100)
        return self.price

