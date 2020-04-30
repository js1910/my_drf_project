from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='名字', max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    vnum = models.IntegerField(verbose_name='浏览量')
    content = models.TextField(verbose_name='内容')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='articles') # related_name 反向查找

    def __str__(self):
        return self.title


