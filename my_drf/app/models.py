from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(verbose_name='名字', max_length=100)


class Student(models.Model):
    name = models.CharField(verbose_name='名字', max_length=100)
    age = models.IntegerField(verbose_name='年龄')
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
