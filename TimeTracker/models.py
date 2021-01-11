from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=65)
    position = models.CharField(max_length=50)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    start_time = models.DateTimeField(auto_now_add=False, blank=False)
    end_time = models.DateTimeField(auto_now_add=False, blank=False)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


# @receiver(post_save, sender =User)
# def create_user_employee(instanc, created, **kwargs):
#     if created:
#         Employee.object.create(
#             name=instanc
#         )