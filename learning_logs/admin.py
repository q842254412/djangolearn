from django.contrib import admin

# Register your models here.
from django.contrib import admin #自动化站点管理工具用于管理Django网站后台
from .models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)