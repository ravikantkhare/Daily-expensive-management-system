from django.contrib import admin
from .models import User,Expence,Income
# Register your models here.
admin.site.register(Expence)
admin.site.register(Income)
@admin.register(User) 
# @admin.register(Expence) 
class useradmin(admin.ModelAdmin):
    list_display=['uname','age','upassword','mobile','address']
# class Expenceadmin(admin.ModelAdmin):
#     list_display=['time','date','remark','amount','category']
    
