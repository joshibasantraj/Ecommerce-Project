from django.urls import path
from . import views

urlpatterns = [
    path('suscribe/',views.SuscribeCreate.as_view(),name="suscribe"),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('contact-create/',views.ContactCreate.as_view(),name="contact-create"),
    path('about/',views.AboutView.as_view(),name="about"),
    path('search/',views.SearchView.as_view(),name="search"),



    path('admin-login/',views.AdminLogin.as_view(),name="admin-login"),
    path('admin-logout/',views.AdminLogout.as_view(),name="admin-logout"),
    path('',views.HomeView.as_view(),name="home"),
    path('products/',views.ProductView.as_view(),name="products"),
    path('product-detail/<int:pk>/',views.ProductDetail.as_view(),name="product-detail"),





    path('dashboard/',views.DashboardView.as_view(),name="dashboard"),
    path('banner-list/',views.BannerList.as_view(),name="banner-list"),
    path('banner-create/',views.BannerCreate.as_view(),name="banner-create"),
    path('banner-update/<int:pk>/',views.BannerUpdate.as_view(),name="banner-update"),
    path('banner-delete/<int:pk>/',views.DeleteBanner.as_view(),name="banner-delete"),

    path('category-list/',views.CategoryList.as_view(),name="category-list"),
    path('category-create/',views.CategoryCreate.as_view(),name="category-create"),
    path('category-update/<int:pk>/',views.CategoryUpdate.as_view(),name="category-update"),
    path('category-delete/<int:pk>/',views.CategoryDelete.as_view(),name="category-delete"),


    path('product-list/',views.ProductListView.as_view(),name="product-list"),
    path('product-create/',views.ProductCreateView.as_view(),name="product-create"),
    path('product-update/<int:pk>/',views.ProductUpdateview.as_view(),name="product-update"),
    path('product-delete/<int:pk>/',views.ProductDeleteView.as_view(),name="product-delete"),

    path('admin-order/',views.OrderView.as_view(),name="order-list"),
    path('order_update/<int:pk>/',views.AdminOrderUpdateView.as_view(),name="order-update"),
    path('order-delete/<int:pk>/',views.AdminOrderDelete.as_view(),name="order-delete"),

    path('admin-review/',views.AdminReview.as_view(),name="admin-review"),
    path('review-delete/<int:pk>/',views.AdminReviewDelete.as_view(),name="review-delete"),






    path('mycart/',views.MyCart.as_view(),name="mycart"),
    path('shopping-cart-<int:id>/',views.AddToCartView.as_view(),name="shopping-cart"),
    path('manage-cart-<int:id>/',views.ManageCartView.as_view(),name="manage-cart"),


    path('checkout/',views.CheckOutView.as_view(),name="checkout"),



    path('customer-registration/',views.CustomerRegistration.as_view(),name="customer-registration"),
    path('customer-login/',views.CustomerLoginView.as_view(),name="customer-login"),
    path('customer-logout/',views.CustomerLogoutView.as_view(),name="customer-logout"),


    path('review/',views.ReviewCreateView.as_view(),name="review"),
]
