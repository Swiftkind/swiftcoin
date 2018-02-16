import hashlib
from django.db import models


class Account(models.Model):
    """ swiftcoin users
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"({self.full_name}) {self.address}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.address = self.generate_address()
        return super(Account, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def generate_address(self):
        sha = hashlib.sha256()
        sha.update(str.encode(f"{self.id}{self.first_name}{self.last_name}"))

        return sha.hexdigest()