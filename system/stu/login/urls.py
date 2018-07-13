from django.conf.urls import url
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^student/$',login_stu_views),
    url(r'^teacher/$',login_teacher_views),
]