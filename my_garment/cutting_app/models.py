from importlib.resources import contents
from django.conf import settings   
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.db.models.signals import pre_save,post_save
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect
from django.utils import timezone
from .utils import slugify_instance_title
#

User = settings.AUTH_USER_MODEL
class ArticleQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)
class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model,using=self._db)
    def search(self,query=None):
        return self.get_queryset().search(query=query)
       
class Articles(models.Model):
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.SET_NULL)
    title= models.TextField()
    slug = models.SlugField(unique=True,blank=True,null=True)
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish= models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True )
    objects = ArticleManager()
    def get_absolute_url(self):
        return reverse('garment:article-detail',kwargs={"slug":self.slug})
    def save(self,*args,**kwargs):
        # obj = Articles.objects.get(id=1)
        #set something
        # if self.slug is None:
        #   self.slug = slugify(self.title)
        # if self.slug is None:
        #     slugify_instance_title(self,save=False)
        super().save(*args,**kwargs) 
        # obj.save()
        # do another something

def article_pre_save(sender,instance , *args,**kwargs):
    print("pre_save")
    if instance.slug is None:
        slugify_instance_title(instance,save=False)


pre_save.connect(article_pre_save,sender=Articles)

def article_post_save(sender,instance,created,*args,**kwargs):
    print("post_save")
    if created:
        slugify_instance_title(instance,save=True)
post_save.connect(article_post_save,sender=Articles)

class Employee(models.Model):
    emp_name = models.CharField(max_length=100,unique=True,verbose_name="إسم الموظف")
    password = models.CharField(max_length=30,verbose_name="كلمة المرور")
    phone = models.CharField(max_length=12)
    birth_day = models.DateField(default=timezone.now,verbose_name="تأريخ الميلاد")
    email = models.EmailField(verbose_name="الأيميل")
    status = models.BooleanField(verbose_name="الحاله")
    def __str__(self):
        return self.emp_name
class PhonesNumber(models.Model):
    phoneNumber = models.CharField(max_length=15,unique=True)
class Customer(models.Model):
    fname= models.CharField(max_length=100,unique=True)
    lname = models.CharField(max_length=100)
    Password = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.ForeignKey(PhonesNumber,on_delete=models.PROTECT)
    email = models.EmailField()
    status = models.BooleanField()
    def  __str__(self):
        return self.fname + self.lname
class Stock(models.Model):
    stock_id = models.IntegerField(verbose_name=" رقم المخزن" )
    stock_name= models.CharField(max_length=100,null=True)
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.stock_name)

    def save(self,*args,**kwargs):
        
        # if self.note is None:
        #     self.note = self.stock_name
        super().save(*args,**kwargs)

      