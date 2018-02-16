from rest_framework import serializers

from blockchain.chain import Chain
from .models import Account


class AccountSerializer(Chain, serializers.ModelSerializer):
    
    coins = serializers.SerializerMethodField()

    def get_coins(self, obj):
        return self.get_balance(obj.address)

    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'address', 'coins')