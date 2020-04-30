from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)  # 更新时间
    isdelete = models.BooleanField(verbose_name='是否删除', default=False)  # 是否删除

    class Meta:
        abstract = True
# 普通
class Cross(BaseModel):
    title = models.CharField(verbose_name='标题',max_length=100)
    content = models.CharField(verbose_name='内容',max_length=4000)

# 图片
class PicturesCross(BaseModel):
    title = models.CharField(verbose_name='标题',max_length=100)
    content = models.CharField(verbose_name='内容',max_length=400)
    cover = models.ImageField(verbose_name='图片',upload_to='banner/%Y/%m/%d')

# 热门
class HotCross(BaseModel):
    title = models.CharField(verbose_name='标题',max_length=100)
    content = models.CharField(verbose_name='内容',max_length=4000)
    istop = models.BooleanField(verbose_name='是否置顶', default=False)


# 点赞
class Goods(models.Model):
    cross = models.ManyToManyField(to=Cross,related_name='cross')
    picturescross = models.ManyToManyField(to=PicturesCross,related_name='picturescross')
    hotcross = models.ManyToManyField(to=HotCross,related_name='hotcross')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

