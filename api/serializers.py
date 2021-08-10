from rest_framework import serializers
from ecom.models import Banner,Category,Product,ProductImages,Cart,CartProduct,Order,Customer,CustomerReview,UserImage,ContactUs,Suscribe
from django import forms

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields='__all__'


class SuscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Suscribe
        fields='__all__'

class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerReview
        fields='__all__'

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserImage
        fields='__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','user','fullname','address']



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImages
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    # # images=serializers.StringRelatedField(many=True,read_only=True)
    # more_images=serializers.FileField()
    class Meta:
        model=Product
        fields=['title','slug','category','image','status','marked_price','selling_price','description','warrenty','return_policy']
        # include=['images']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['id','customer','total']


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartProduct
        fields='__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','cart','ordered_by','shipping_address','mobile','email','subtotal','discount','total']