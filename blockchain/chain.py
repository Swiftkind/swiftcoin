import hashlib

from django.utils import timezone
from .models import Transaction, Block


class Chain(object):
    """ manages blockchains
        NOTE: right now it only has one block chain
    """
    def __init__(self, *args, **kwargs):
        return super(Chain, self).__init__(*args, **kwargs)

    def _get_total_coins(self, **kwargs):
        return sum(Transaction.objects.filter(**kwargs).values_list('amount', flat=True))

    def coins_acquired(self, user):
        return self._get_total_coins(recipient=user)

    def coins_transferred(self, user):
        return self._get_total_coins(sender=user)

    def get_balance(self, user):
        return self.coins_acquired(user) - self.coins_transferred(user)

    def sender_balance_valid(self, user, amount):
        if self.get_balance(user) >= amount:
            return True
        return False

    def get_prev_hash(self):
        return Block.objects.last().secret

    def generate_hash(self, block, trans):
        from .serializers import TransactionSerializer

        data = TransactionSerializer(trans, many=True).data

        sha = hashlib.sha256()
        sha.update(str.encode(
            f"{block.id}{block.timestamp}{data}{block.previous_hash}"))

        return sha.hexdigest()

    def new_block(self, recipient, proof):
        """ create a new block
        """
        block = Block.objects.create(
            previous_hash=self.get_prev_hash(), proof=proof)

        transactions = Transaction.objects.all()
        block.transactions.add(*transactions)

        block.secret = self.generate_hash(block, transactions)
        block.save()

        return block



class Mine(object):
    """ let's mine mine mine!

        NOTE: THIS IS JUST A CONCEPT
    """
    def __init__(self, *args, **kwargs):
        return super(Mine, self).__init__(*args, **kwargs)

    @property
    def previous_proof(self):
        """ return the latest pow
        """
        return Block.objects.last().proof

    def proof_is_found(self, proof):
        return proof

    def generate_pow(self, miner):
        """ start the algorithm
        """
        timestart = timezone.now()
        magicnumber = self.previous_proof + 1 # so that it will start on the next number

        # do the magic until the correct number appears
        while not (magicnumber % 13 == 0 and magicnumber % self.previous_proof == 0):
            magicnumber += 1

        return magicnumber