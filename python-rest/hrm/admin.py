from django.contrib import admin
from hrm.models import User
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from django.utils.html import format_html
# Register your models here.


    
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).capitalize()
upper_case_name.short_description = 'Name'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',upper_case_name, 'email','is_active','is_staff','Keywordd')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('is_active','is_staff')
    upper_case_name.admin_order_field = 'first_name'

    def Keywordd(self, obj):
        return format_html('<a class="user-detail" data-id =%s  href="#">%s</a>' % (obj.id, 'detail'))
        
    Keywordd.allow_tags = True
    Keywordd.admin_order_field = 'ProjectKW'
    Keywordd.short_description = 'ProjectKW'
    # ordering = ['Name']



admin.site.register(User,UserAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)