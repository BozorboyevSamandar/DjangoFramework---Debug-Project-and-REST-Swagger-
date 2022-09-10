from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ToppingSerializer, PizzaSerializer, ZakazSerializer
from basic.models.models import Topping, Pizza, Zakaz


class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    # queryset = Pizza.objects.all().prefetch_related('toppings')
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    @action(['GET'], detail=False)
    def get_pizza(self, request):
        queryset = self.get_queryset()
        for i in queryset:
            return Response({"success": "DONE"})


class ZakazViewSet(viewsets.ModelViewSet):
    # queryset = Zakaz.objects.all()
    queryset = Zakaz.objects.select_related('user')
    serializer_class = ZakazSerializer

    @action(['GET'], detail=False)
    def get_users_username(self, request):
        queryset = self.get_queryset()
        for i in queryset:
            # print(i.user.username)
            return Response({"success": "DONE"})













# from .serializers import CartItemSerializer
# from .models import CartItem
# # class CartItemViews(APIView):
# @api_view(['GET', 'POST'])
# def post(request):
#     print(request.method, "+++++++++++++++")
#     if request.method == 'POST':
#         serializer = CartItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         data = CartItem.objects.all()
#         serializer = CartItemSerializer(data, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def get_detail(request, pk):
#     data_id = CartItem.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = CartItemSerializer(data_id)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CartItemSerializer(data_id, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     elif request.method == 'DELETE':
#         data_id.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
