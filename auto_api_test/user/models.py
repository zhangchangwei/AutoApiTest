from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name =  None
    last_name =   None
    is_staff =  None

    username = models.CharField(max_length=50, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=50, verbose_name="密码")
    nick_name = models.CharField(max_length=50, verbose_name="昵称")
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(max_length=6, choices=(
        ('male', '男'),
        ('female', '女')
    ))
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    email =  models.EmailField()
    last_login = models.DateField()
    is_superuser =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField()

    groups =  None
    user_permissions = None
