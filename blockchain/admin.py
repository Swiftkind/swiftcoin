from django.contrib import admin
from .models import Transaction, Block


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('id', 'sender', 'recipient', 'amount', 'date_created')


class BlockAdmin(admin.ModelAdmin):
    model = Block
    list_display = ('id', 'timestamp', 'previous_hash', 'secret', 'proof')


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Block, BlockAdmin)