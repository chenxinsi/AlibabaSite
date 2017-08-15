from django.db import models


class Users(models.Model):
    id = models.IntegerField(u'id',primary_key=True)
    name = models.CharField(u'name',max_length=256)
    passwd = models.CharField(u'passwd',max_length=256)
    def __str__(self):
        return self.passwd

# Create your models here.
