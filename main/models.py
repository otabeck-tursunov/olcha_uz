from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models import Account, Seller


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sub-categories/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(default=0)

    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    main = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class ProductColor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product-colors/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ParameterChoice(models.Model):
    value = models.CharField(max_length=255)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='comments/')
    rate = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


