from django.shortcuts import render

# Create your views here.
from src.apps.product.serializers import ProductSerializer, ProductDetailsSerializer
from src.apps.product.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from src.apps.account.serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from ..account import serializers 


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer





class ProductView(ListAPIView):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetailView(RetrieveAPIView):

    serializer_class = ProductDetailsSerializer
    queryset = Product.objects.all()



class AddToFavorite(APIView):
    def post(self, request, pk):
        user = request.user  
        product = get_object_or_404(Product, pk=pk)
        user.favorite_choice.add(product)
        return Response({"message": "Товар успешно добавлен в список избранных."}, status=status.HTTP_200_OK)


class RemoveFromFavorite(APIView):
    def delete(self, request, pk):
        user = request.user  
        product = get_object_or_404(Product, pk=pk)
        user.favorite_choice.remove(product)
        return Response({"message": "Товар успешно удален из списка избранных."}, status=status.HTTP_200_OK)


class RegisterUser(CreateAPIView):
    serializer_class = serializers.RegisterUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'details': 'Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
