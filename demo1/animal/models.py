from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Classify(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Label(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Article(models.Model):
    title=models.CharField(max_length=30)
    body=models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='ads',verbose_name='图片')
    desc=models.CharField(max_length=30,verbose_name='描述')
    label=models.ManyToManyField(Label)
    num=models.PositiveIntegerField(default=0)
    classify=models.ForeignKey(Classify,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '文章'
        verbose_name_plural = verbose_name

class Album(models.Model):
    img=models.ImageField(upload_to='ads',verbose_name='图片')
    desc=models.CharField(max_length=30,verbose_name='描述')

    def __str__(self):
        return self.desc

    class Meta():
        verbose_name = '图片集'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    name=models.CharField(max_length=30,)
    email = models.EmailField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    message=models.TextField()
    article=models.ForeignKey(Article,on_delete=models.CASCADE)


class Img(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name='图片')
    desc = models.CharField(max_length=30, verbose_name='描述')
    def __str__(self):
        return self.desc

    class Meta():
        verbose_name = '相册集'
        verbose_name_plural = verbose_name
