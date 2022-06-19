from django.contrib import admin
from . models import *
# Register your models here.

class ApiAdmin(admin.ModelAdmin):
	list_display = ('id','name')

admin.site.register(Api, ApiAdmin)
