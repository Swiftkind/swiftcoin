import hashlib
from django.db import models


class Transaction(models.Model):
    """ transaction
    """
    sender = models.CharField(max_length=250)
    recipient = models.CharField(max_length=250)
    amount = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.amount}) {self.recipient}"


class Block(models.Model):
    """ block
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    previous_hash = models.TextField("Previous Hash")
    secret = models.TextField("Hash")
    
    transactions = models.ManyToManyField(Transaction, blank=True)
    proof = models.PositiveIntegerField()

    def __str__(self):
        return f"(BLOCK {self.id}) : {self.secret}"