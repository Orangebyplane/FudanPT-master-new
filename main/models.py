from django.db import models

# Create your models here.

#建数据库
class data_rank(models.Model):
    number=models.IntegerField()
    type=models.IntegerField()
    grade=models.IntegerField()