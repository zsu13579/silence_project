# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'student'

class Testuserout(models.Model):
    provcd = models.IntegerField(blank=True, null=True)
    provnm = models.CharField(max_length=40, blank=True, null=True)
    imsi = models.BigIntegerField(blank=True, null=True)
    cdrall = models.BigIntegerField(blank=True, null=True)
    cdrvoice = models.BigIntegerField(blank=True, null=True)
    cdrdata = models.BigIntegerField(blank=True, null=True)
    cdr23g = models.BigIntegerField(blank=True, null=True)
    cdr4g = models.BigIntegerField(blank=True, null=True)
    callduration = models.BigIntegerField(blank=True, null=True)
    smsmo = models.BigIntegerField(blank=True, null=True)
    smsmt = models.BigIntegerField(blank=True, null=True)
    data = models.BigIntegerField(blank=True, null=True)
    data23g = models.BigIntegerField(blank=True, null=True)
    data4g = models.BigIntegerField(blank=True, null=True)
    chgrmb = models.BigIntegerField(blank=True, null=True)
    unichg = models.BigIntegerField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    carriers = models.IntegerField(blank=True, null=True)
    countrys = models.IntegerField(blank=True, null=True)
    country_list = models.CharField(max_length=500, blank=True, null=True)
    lastcalldt = models.IntegerField(blank=True, null=True)
    issilence = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'testuserout'
        ordering = ['-days','-lastcalldt']

class Testuseroutold(models.Model):
    sttldt = models.IntegerField(blank=True, null=True)
    callstartdt = models.IntegerField(blank=True, null=True)
    carriercd = models.CharField(max_length=5, blank=True, null=True)
    provcd = models.IntegerField(blank=True, null=True)
    imsi = models.BigIntegerField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    data = models.BigIntegerField(blank=True, null=True)
    cdr = models.IntegerField(blank=True, null=True)
    provsdr = models.IntegerField(blank=True, null=True)
    provrmb = models.IntegerField(blank=True, null=True)
    carriercdr = models.IntegerField(blank=True, null=True)
    carrierrmb = models.IntegerField(blank=True, null=True)
    unichg = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'testuseroutold'

class Callhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    calldate = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    # imsi = models.ForeignKey('Testuserout', models.DO_NOTHING, db_column='imsi')
    imsi = models.BigIntegerField()

    class Meta:
        db_table = 'callhistory'

class Activateuserinfo(models.Model):
    countall = models.IntegerField(blank=True, null=True)
    countactivate = models.IntegerField(blank=True, null=True)
    unichg = models.IntegerField(blank=True, null=True)
    smsmo = models.IntegerField(blank=True, null=True)
    callduration = models.IntegerField(blank=True, null=True)
    data = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'activateuserinfo'

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.name
