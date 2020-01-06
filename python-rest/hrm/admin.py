from django.contrib import admin
from hrm.models import User
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
# Register your models here.


    
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).capitalize()
upper_case_name.short_description = 'Name'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',upper_case_name, 'email','is_active','is_staff')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('is_active','is_staff')
    upper_case_name.admin_order_field = 'first_name'
    # ordering = ['Name']



admin.site.register(User,UserAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)