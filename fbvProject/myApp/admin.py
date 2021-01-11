from django.contrib import admin
from myApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	a=['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)