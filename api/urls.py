from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router=DefaultRouter()

router.register('bannerapi',views.BannerViewSet,basename="bannerapi")
router.register('categoryapi',views.CategoryViewSet,basename="categoryapi")
router.register('productapi',views.ProductViewSet,basename='productapi')
router.register('cartapi',views.CartViewSet,basename="cartapi")
router.register('cartproduct',views.CartProductViewSet,basename="cartproduct")
router.register('order',views.OrderViewSet,basename='order')
router.register('customer',views.CustomerViewSet,basename='customer')
router.register('userimage',views.UserImageViewSet,basename='userimage')
router.register('customerreview',views.CustomerReviewViewSet,basename='customerreview')
router.register('contactus',views.ContactUsViewSet,basename='contactus')
router.register('suscribe',views.SuscribeViewSet,basename='suscribe')


urlpatterns = [
    path('',include(router.urls)),
    path('token-obtain/',TokenObtainPairView.as_view(),name="token-obtain"),
    path('token-refresh/',TokenRefreshView.as_view(),name="token-refresh"),
    path('token-verify',TokenVerifyView.as_view(),name="token-verify"),
]
