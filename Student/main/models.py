# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Students(models.Model):
	name = models.CharField(max_length = 100)
	uin = models.CharField(max_length = 100)
	year = models.IntegerField()
	def __str__(self):
		return self.name


