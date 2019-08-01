from django.db import models

# Create your models here.

class Level(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64,verbose_name="等级名称")
    experience=models.IntegerField(max_length=32,verbose_name="所需经验值")
    upper_level=models.ForeignKey(to="Level",on_delete=False,verbose_name="上一级",related_name="next_level")
    introduce=models.CharField(max_length=128,verbose_name="等级简介")

class Varieties(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name="品种名称")

class Cat(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name="喵名字")
    varieties=models.ForeignKey(to="Varieties",on_delete=False,verbose_name="关联品种",related_name="cat")
    age=models.DateTimeField(auto_now_add=False,auto_created=False)
    gender_choice=((1,"公"),(2,"母"))
    gender=models.CharField(max_length=32,choices=gender_choice)
    number_of_vaccines=models.IntegerField(max_length=32,verbose_name="疫苗次数")


class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=64,verbose_name="用户名")
    password=models.CharField(max_length=64,verbose_name="密码")
    phone=models.CharField(max_length=64,verbose_name="手机号")
    email=models.EmailField(verbose_name="邮箱")
    experience=models.IntegerField(max_length=32,verbose_name="经验值")
    cat=models.ForeignKey(to="Cat",on_delete=False,verbose_name="所有的猫咪",related_name="user")

class EquipmentType(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64,verbose_name="装备属性值类型")

class Equipment(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64,verbose_name="装备名称")
    attribute_value=models.FloatField(max_length=64,verbose_name="增加属性值")
    type=models.ForeignKey(to="EquipmentType",on_delete=False,verbose_name="属性值类型",related_name="eq")


