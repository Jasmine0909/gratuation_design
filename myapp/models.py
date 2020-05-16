from django.db import models

# Create your models here.


class User(models.Model):

    GENDER_CHOICES = (
        ('male', "男"),
        ('female', "女"),
        ('secret', "保密")
    )

    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)
    telephone = models.CharField(max_length=11, blank=True)
    consignee = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="secret")
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Goods(models.Model):
    name = models.CharField(max_length=10, blank=False)
    # 商品分类
    classify = models.CharField(max_length=10, blank=True)
    # 功效
    function = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=10, blank=False)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return self.name

    pass

