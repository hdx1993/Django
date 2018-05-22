from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add', views.add_students, name='add'),
    url(r'^del', views.del_students, name='del'),

]
