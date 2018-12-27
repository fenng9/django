from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
    查询使用的几种方法:
    1,插入数据: Post.objects.create()
    2,查询数据: Post.objects.all()
    3,过滤数据: Post.objects.filter(publish__year=2015,author__username='admin')
    4,排除数据: Post.objects.filter(publish__year=2015).exclude(title__startswith='Why')
    5,排序数据: Post.objects.order_by('title')
    6,删除数据：post = Post.ojects.get(id=1); post.delete()
    可参考:https://yiyibooks.cn/xx/Django_1.11.6/index.html
"""

class PublishedManager(models.Manager):
    '''自定义管理器'''
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    objects = models.Manager() #默认管理器，Post.objects.all()
    published = PublishedManager() #自定义管理器,Post.published.all()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

