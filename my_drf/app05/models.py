from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)  # 更新时间
    isdelete = models.BooleanField(verbose_name='是否删除', default=False)  # 是否删除
    class Meta:
        abstract = True

class Category(models.Model):
    desc = models.CharField(verbose_name='分类',max_length=20)

class Tags(models.Model):
    tag = models.CharField(verbose_name='标签',max_length=20)

class News(models.Model):
    title = models.CharField(verbose_name='标题',max_length=100)
    content = models.CharField(verbose_name='内容',max_length=4000)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='news')
    tag = models.ManyToManyField(to=Tags,related_name='news')
    user = models.ForeignKey(to='auth.User',on_delete=models.CASCADE)


















