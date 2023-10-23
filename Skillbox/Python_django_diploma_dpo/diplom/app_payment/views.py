from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response
from app_basket.models import Cart


class PaymentWithOut(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        cart = Cart(request)
        cart.clear()
        return Response(status=HTTP_200_OK)
