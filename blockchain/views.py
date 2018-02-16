from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import TransactionSerializer, SmashSomeRocks


class Coin(ViewSet):
    """ coin actions
    """
    serializer_class = TransactionSerializer

    def send(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class MiningArea(ViewSet):
    """ mining is actually not mining but working to
        maintain the block's consistency
    """
    serializer_class = SmashSomeRocks

    def smash_rocks(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #import pdb;pdb.set_trace()

        return Response(serializer.data, status=200)