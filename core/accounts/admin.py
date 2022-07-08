from django.contrib import admin
from accounts.models import User
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',  'first_name', 'last_name','last_login', 'date_joined')


admin.site.register(User, UserAdmin)