from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from django.shortcuts import get_object_or_404
from .serializers import AccountSerializer
from .models import Account


class User(ViewSet):
    """ user data
    """
    serializer_class = AccountSerializer

    def status(self, *args, **kwargs):
        address = self.request.query_params.get('address')

        serializer = self.serializer_class(
            get_object_or_404(Account, address=address))

        return Response(serializer.data, status=200)