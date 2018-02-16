from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('id', 'first_name', 'last_name', 'address')


admin.site.register(Account, AccountAdmin)