from django.db import models

# Create your models here.


class Person(models.Model):
    class Person(models.Model):
        name = models.CharField(max_length=30)
        age = models.IntegerField()

        def __unicode__(self):
            # 在Python3中使用 def __str__(self):
            return self.name
