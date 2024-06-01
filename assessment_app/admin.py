from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Userdetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'password', 'created_dt']

@admin.register(FrndRequest)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','fk_user', 'fk_request_user', 'request_status', 'created_dt']