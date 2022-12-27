from multiprocessing import Condition
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.deletion import SET_NULL


class Customer(models.Model):
    firstName = models.CharField(max_length=15, null=True, blank=True)
    lastName = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=10, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Add(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    cus = models.ForeignKey(Customer, on_delete=SET_NULL, null=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class AddPic(models.Model):
    add = models.ForeignKey(Add, on_delete=SET_NULL, null=True)
    pic = models.ImageField(blank=True, null=True)
    pic2 = models.ImageField(blank=True, null=True)
    pic3 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
