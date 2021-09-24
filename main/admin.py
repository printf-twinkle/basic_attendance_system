from django.contrib import admin

from main.models import User 


class UserAdmin(admin.ModelAdmin):

    list_filter = ['name','username','email','roll_number','is_student','is_teacher']
    list_display = ['name','username','email','roll_number','is_student','is_teacher']
    search_fields = ['name','username','email','roll_number','is_student','is_teacher']
    class Meta:
        model = User


admin.site.register(User, UserAdmin)

 