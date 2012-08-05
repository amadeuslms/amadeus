from django.contrib import admin
from core.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'sex', 'birthday', 'profileImage', 'createdAt')

admin.site.register(User, UserAdmin)