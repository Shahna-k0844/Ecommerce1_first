from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categories(models.Model):
    name=models.CharField(max_length=200)
    image=models.FileField(upload_to='categories\images')
    def __str__(self):
        return self.name
    
    
class products(models.Model):
    Category=models.ForeignKey(categories,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    rate=models.IntegerField()
    image=models.FileField(upload_to='products\images')
    color = models.CharField(max_length=50, default="")
    # size = models.CharField(max_length=50)
    # shipping_info = models.TextField()
    # offers = models.TextField()
    care_instructions = models.TextField(default="")
    design = models.CharField(max_length=100,null=True)
    fabric = models.CharField(max_length=100,default="")
    # sleeve_length = models.CharField(max_length=50)
    pattern = models.CharField(max_length=100,default="")
    country_of_origin = models.CharField(max_length=100,default="")
    description=models.TextField(default="")
    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(products, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField()

    def __str__(self):
        return f"{self.product.name} ( {self.quantity} )"
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(products, on_delete=models.CASCADE)
    # quantity=models.PositiveIntegerField(default=1)
    # price=models.IntegerField()

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(default="")
    # def get_total_price(self):
    #     return sum(i.totalprice() for i in self.Cart_item.set.all())
        
    

