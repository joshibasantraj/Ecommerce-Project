from rest_framework import viewsets
from ecom.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication



class ContactUsViewSet(viewsets.ModelViewSet):
    queryset=ContactUs.objects.all()
    serializer_class=ContactUsSerializer


class SuscribeViewSet(viewsets.ModelViewSet):
    queryset=Suscribe.objects.all()
    serializer_class=SuscribeSerializer


class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset=CustomerReview.objects.all()
    serializer_class=CustomerReviewSerializer


class UserImageViewSet(viewsets.ModelViewSet):
    queryset=UserImage.objects.all()
    serializer_class=UserImageSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class CartProductViewSet(viewsets.ModelViewSet):
    queryset=CartProduct.objects.all()
    serializer_class=CartProductSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

