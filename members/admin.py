from django.contrib import admin
from .models import Members,Employees,Products,Users


# Register your models here.


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","phone","test")

admin.site.register(Members, MemberAdmin)

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname")

admin.site.register(Employees,EmployeeAdmin)


admin.site.register(Products)


class Useradmin(admin.ModelAdmin):
  list_display = ("username", "password","user_image")
admin.site.register(Users,Useradmin)
