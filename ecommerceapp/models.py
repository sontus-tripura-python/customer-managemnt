from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    CATEGORY = (
     ('Indoor', 'Indoor'),
     ('Out of Door', 'Out of Door'),

    )
    product_name = models.CharField(max_length=200, null=True)
    product_price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    STATUS = (

    ('Pending', 'Pending'),
    ('Out of Delivery', 'Out of Delivery'),
    ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(product, null=True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.product_name
