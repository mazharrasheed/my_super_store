from django.contrib import admin
from .models import Members,Employees


# Register your models here.


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","phone","test")

admin.site.register(Members, MemberAdmin)

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname")

admin.site.register(Employees,EmployeeAdmin)
