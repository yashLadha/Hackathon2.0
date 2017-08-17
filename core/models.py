# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_elasticsearch.models import EsIndexable


class User(EsIndexable, models.Model):
    """Model representation of the User
    Index: django
    """
    name_eng = models.CharField(default=None, max_length=150, blank=False, null=False)
    aadhaar_id = models.CharField(default=None, max_length=12)
    m_id = models.IntegerField(default=0)
    name_hnd = models.CharField(default=None, max_length=150)
    gender = models.CharField(default=None, max_length=10)
    dob = models.DateField(default=None, null=True)
    hof = models.BooleanField(default=False, blank=True)
    family_id = models.CharField(default='', max_length=12)

    def __str__(self):
        return str(self.id) + '/' + self.name_eng

    @staticmethod
    def get_count_user():
        return User.es.count()


class BhamashahIndex(models.Model):
    """Model representation for Bhamashah lookup
    Index : bhamashah
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bhamashah_id = models.CharField(max_length=15, default='')


class LocHof(models.Model):
    """Model representation for location of hof
    Index: location
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pincode = models.IntegerField()
