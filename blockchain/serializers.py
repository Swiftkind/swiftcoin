from rest_framework import serializers
from .models import Block, Transaction

from .chain import Chain, Mine


class TransactionSerializer(Chain, serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'sender', 'recipient', 'amount', 'date_created')

    def validate(self, data):
        """ validate through the blockchain network
            if the transaction is valid.
        """
        sender = data.get('sender')
        amount = data.get('amount')

        if not self.sender_balance_valid(sender, amount):
            raise serializers.ValidationError("Sender doesn't have enough coins")

        return data


class SmashSomeRocks(Mine, Chain, serializers.ModelSerializer):

    timestamp = serializers.DateTimeField(read_only=True)
    previous_hash = serializers.CharField(read_only=True)
    secret = serializers.CharField(read_only=True)
    proof = serializers.IntegerField(read_only=True)
    recipient = serializers.CharField(write_only=True)

    transactions = TransactionSerializer(read_only=True, many=True)

    class Meta:
        model = Block
        fields = ('timestamp', 'previous_hash', 'secret', 'transactions', 'proof', 'recipient')

    def create(self, data):
        """ create a new block
        """
        recipient = data.get('recipient')
        proof = self.generate_pow(data)

        if not self.proof_is_found(proof):
            raise serializers.ValidationError("Ooops something's fishy is going on.")

        # create a new transaction
        Transaction.objects.create(sender="Swiftkind Network",
            recipient=recipient, amount=1)

        # create a new block
        block = self.new_block(recipient, proof)

        return block