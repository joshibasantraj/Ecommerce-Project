from django.contrib import admin
from .models import Suscribe,ContactUs,UserImage,Banner,Category,Product,ProductImages,Customer,Cart,CartProduct,Order,CustomerReview

# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display=['title','status','image','added_by']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','is_parent','image','parent_id','status']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title']
    
@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    list_display=['product']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','fullname','address']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_diplay=['customer','total']

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display=['cart','product','rate','quantity','subtotal']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['cart','ordered_by','shipping_address','mobile','email','subtotal','discount','total','order_status']


@admin.register(CustomerReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['product','rating','review','name','email']

@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display=['user','image']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['email','msg']

@admin.register(Suscribe)
class SuscribeAdmin(admin.ModelAdmin):
    list_display=['email']