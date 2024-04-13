from django.contrib import admin
from .models import *
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "standard"] 
    
    # ordering = ['id']


class gradeAdmin(admin.ModelAdmin):
    list_display = ["id", "grade"] 
    ordering = ['id']



admin.site.register(Student, studentAdmin)
admin.site.register(Grade, gradeAdmin)
admin.site.register(IsPassed)

# class userAdminConfig(UserAdmin):  
#     search_fields = ['email', 'username', 'firstname']
#     ordering = ('firstname',)
#     list_display = ['email', 'username', 'firstname', 'is_active', 'is_staff']
#     list_filter = ['email', 'username', 'firstname', 'is_active', 'is_staff']
#     fieldsets = (
#         ('details', {"fields": ('email', 'username', 'firstname')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')})
#     )