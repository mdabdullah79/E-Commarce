from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=length, ${blank=True,null=True})
    
    price = models.IntegerField()
    discount_price = models.IntegerField()
    slug = models.SlugField()
    def __str__(self):
        return self.user.title


class OrderItem(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    item = models.ForeignKey(item,on_delete=models.CASCADE)
    Ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"



class Order(models.Model):
    user = models.name = models.ForeignKey(user,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    Ordered = models.BooleanField(default=False)
    _state_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateField()

    def __str__(self):
        return self.user.username
