from django.contrib import admin
from .models import (User, Subscription)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username',)
    search_fields = ('email',)
    list_filter = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Subscription)
