from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(verbose_name='游戏名字', max_length=10)
    desc = models.CharField(verbose_name='描述', max_length=20)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class News(models.Model):
    title = models.CharField(verbose_name='标题',max_length=20)
    content = models.CharField(verbose_name='内容',max_length=400)


class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField('auth.User',models.CASCADE) # 一个用户只能有一个token
    token = models.CharField(max_length=64)



