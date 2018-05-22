# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Students
from django.http import HttpResponseRedirect  
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	allstudents = Students.objects.all()
	return render(request, 'index.html', {'student':allstudents})

def add_students(request):
	if (request.method == 'POST'):
		name = request.POST['name_text']
		uin = request.POST['uin_text']
		year = request.POST['year_text']
		new_student = Students(name = name, uin = uin, year = year)
		new_student.save()
		return HttpResponseRedirect('/')
	else:
		return render(request, 'add.html')

def del_students(request):
	if (request.method == 'POST'):
		name = request.POST['name_text']
		# uin = request.POST['uin_text']
		# year = request.POST['year_text']
		del_person = Students.objects.filter(name=name)
		del_person.delete()
		return HttpResponseRedirect('/')
	else:
		return render(request, 'add.html')


# class Stu:
# 	def __init__(self, name, uin, year):
# 		self.name = name
# 		self.uin = uin
# 		self.year = year

# students = [
# 	Stu('Alex', '725008731', 2017),
# 	Stu('Mia','8888385', 2018),
# 	Stu('Yian', '825008731', 2018)

# ]
