from django.shortcuts import render,redirect
from django.views.generic import FormView,TemplateView,DetailView,View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import BannerForm,CategoryForm,ProductForm,CheckOutForm,CustomerRegistrationForm,LoginForm,AdminOrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Suscribe,Banner,Category,Product,ProductImages,Cart,CartProduct,Customer,Order,CustomerReview,ContactUs
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.core.files.storage import default_storage
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models import Q




# Create your views here.
class SuscribeCreate(CreateView):
    model=Suscribe
    fields=['email']
    success_url=reverse_lazy("home")

    
class ContactView(TemplateView):
    template_name="coza/contact.html"

class ContactCreate(CreateView):
    model=ContactUs
    fields=['email','msg']
    success_url=reverse_lazy("home")

class AboutView(TemplateView):
    template_name="coza/about.html"



class SearchView(TemplateView):
    template_name="coza/search.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET['search']
        products=Product.objects.filter(Q(title__icontains=kw) | Q(description__icontains=kw))
        print(products)
        context['products']=products
        return context





class AdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and User.objects.filter(id=request.user.id,is_staff=1).exists():
            pass
        else:
            return redirect("admin-login")
        return super().dispatch(request, *args, **kwargs)
    

class AdminLogin(FormView):
    template_name="useradmin/admin-login.html"
    form_class=LoginForm
    

    def form_valid(self, form):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        # print(user.is_staff)
        if user is not None and user.is_staff:
            login(self.request,user)
            return redirect("dashboard")
        
        return render(self.request,self.template_name,{'form':self.form_class,'error':"InValid Credentials"})
        
        return super().form_valid(form)



class AdminLogout(View):
    def get(self,request):
        logout(self.request)
        return redirect("admin-login")







class DashboardView(AdminMixin,TemplateView):
    template_name='useradmin/base.html'

class BannerList(AdminMixin,ListView):
    template_name="useradmin/banner/index.html"
    model=Banner
    context_object_name="banners"

class BannerCreate(AdminMixin,CreateView,SuccessMessageMixin):
    template_name="useradmin/banner/form.html"
    form_class=BannerForm
    success_url=reverse_lazy('banner-list')
    # success_message = 'Banner Saved Successfully !!!'

    def form_valid(self, form):
        messages.success(self.request,"Bannner created successfully")
        return super().form_valid(form)

class BannerUpdate(AdminMixin,UpdateView):
    template_name="useradmin/banner/form.html"
    form_class=BannerForm
    model=Banner
    success_url=reverse_lazy('banner-list')

    def form_valid(self,form):
        messages.success(self.request,"Banner Updated Successfully")
        print(form)
        return super().form_valid(form)

class DeleteBanner(AdminMixin,DeleteView):
    model=Banner
    success_url=reverse_lazy('banner-list')
    

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"Banner Deleted Successfully")
        return super().post(request, *args, **kwargs)

    # @receiver(post_delete,sender=Banner)
    # # def delete_associated_files(sender,instance,**kwargs):
    # #     path=instance.image.name
    # #     if path:
    # #         default_storage.delete(path)

    # def on_delete(sender, instance,**kwargs):
    #     # instance = kwargs['instance']
    #     instance.image.delete(save=False)

###########################################################################
################### Category Related Views Start ##########################
class CategoryList(AdminMixin,ListView):
    model=Category
    template_name='useradmin/category/index.html'

class CategoryCreate(AdminMixin,CreateView):
    template_name='useradmin/category/form.html'
    form_class=CategoryForm
    success_url=reverse_lazy('category-list')

    def form_valid(self, form):
        messages.success(self.request,"Category Created Successfully")
        return super().form_valid(form)

class CategoryUpdate(AdminMixin,UpdateView):
    model=Category
    template_name='useradmin/category/form.html'
    form_class=CategoryForm
    success_url=reverse_lazy('category-list')

    def form_valid(self, form):
        messages.success(self.request,"Category Updated Successfully")
        return super().form_valid(form)

class CategoryDelete(AdminMixin,DeleteView):
    model=Category
    success_url=reverse_lazy('category-list')

    def post(self, request, *args, **kwargs):
        messages.success(request,"Category Deleted Successfully")
        return super().post(request, *args, **kwargs)



###########################################################################################
############################ Product Views Starts From Here ###############################

class ProductListView(AdminMixin,ListView):
    model=Product
    template_name='useradmin/product/index.html'

class ProductCreateView(AdminMixin,CreateView):
    template_name='useradmin/product/form.html'
    form_class=ProductForm
    success_url=reverse_lazy('product-list')

    def form_valid(self, form):
        messages.success(self.request,"Product Added Successfully !")

        p=form.save()
        images=self.request.FILES.getlist("more_images")
        for i in images:
            ProductImages.objects.create(product=p,image=i)
        return super().form_valid(form)


class ProductUpdateview(AdminMixin,UpdateView):
    template_name='useradmin/product/form.html'
    model=Product
    form_class=ProductForm
    success_url=reverse_lazy('product-list')


    def form_valid(self, form):
        messages.success(self.request,"Product Updated Successfully !")
        p=form.save()
        images=self.request.FILES.getlist("more_images")
        for i in images:
            ProductImages.objects.create(product=p,image=i)
        return super().form_valid(form)


class ProductDeleteView(AdminMixin,DeleteView):
    model=Product
    success_url=reverse_lazy('product-list')

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"Product Deleted Successfully !")
        return super().post(request, *args, **kwargs)



class OrderView(AdminMixin,ListView):
    model=Order
    template_name="useradmin/order/admin_orderlist.html"
    context_object_name="orders"

class AdminOrderUpdateView(AdminMixin,UpdateView):
    model=Order
    form_class=AdminOrderForm
    template_name="useradmin/order/form.html"
    success_url=reverse_lazy("order-list")


    def form_valid(self, form):
        discount=form.cleaned_data["discount"]
        order_id=self.kwargs['pk']
        # print(order_id)
        order_obj=Order.objects.get(id=order_id)
        # print(order_obj.total)
        total=order_obj.total-discount
        form.instance.total=total
        form.save()
        messages.success(self.request,"Order Updated Successfully !!!")
        return super().form_valid(form)


class AdminOrderDelete(AdminMixin,DeleteView):
    model=Order
    success_url=reverse_lazy("order-list")

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"Order Deleted Successfully !!!")
        return super().post(request, *args, **kwargs)


















###############################################################################################################
############################ Front End Views Starts From Here #################################################
class CartMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id=self.request.session.get("cart_id",None)
        if cart_id:
            context["cart"] =Cart.objects.get(id=cart_id) 
        return context
    
class EcomMixin(object):
    def dispatch(self, request, *args, **kwargs):
        cart_id=self.request.session.get("cart_id",None)
        if cart_id:
            cart_obj=Cart.objects.get(id=cart_id)
            if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
                cart_obj.customer=request.user.customer
                cart_obj.save()
        return super().dispatch(request, *args, **kwargs)
    

class HomeView(EcomMixin,CartMixin,TemplateView):
    template_name='coza/index.html'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        banners=Banner.objects.all()
        context['banners']=banners
        context['categories']=Category.objects.all()
        context['products']=Product.objects.all()
        return context


class ProductView(CartMixin,TemplateView):
    template_name='coza/product.html'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['banner']=Banner.objects.all()
        context['categories']=Category.objects.all()
        context['products']=Product.objects.all()
        return context
    



class ProductDetail(EcomMixin,CartMixin,DetailView):
    model=Product
    template_name='coza/product-detail.html'
    context_object_name="product"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        pk=self.kwargs['pk']
        context['productimages']=ProductImages.objects.filter(product=pk)
        product=Product.objects.get(pk=pk)
        product.view_count+=1
        product.save()
        context['product']=product
        reviews=CustomerReview.objects.filter(product=product).all()
        # for review in reviews:
        #     review['rating']=range(review['rating'])
        reviews_count=CustomerReview.objects.count()
        context['reviews_count']=reviews_count
        context['reviews']=reviews
        context['related_products']=Product.objects.filter(category=product.category).all()
        return context

class AddToCartView(EcomMixin,View):
    def get(self,request,*args,**kwargs):
        product_id=self.kwargs['id']
        product_obj=Product.objects.get(id=product_id)
        sp=product_obj.selling_price
        subtotal=sp
        cart_id=self.request.session.get("cart_id",None)
        if cart_id:
            cart_obj=Cart.objects.get(id=cart_id)
            this_product_in_cart=cart_obj.cartproduct_set.filter(product=product_obj)
            if this_product_in_cart.exists():
                cartproduct=this_product_in_cart.last()
                cartproduct.quantity+=1
                cartproduct.subtotal+=sp
                cartproduct.save()
                cart_obj.total+=sp
                cart_obj.save()
            else:
                cartproduct=CartProduct.objects.create(cart=cart_obj,product=product_obj,rate=sp,quantity=1,subtotal=subtotal)
                cart_obj.total+=cartproduct.subtotal
                cart_obj.save()
        else:
            cart_obj=Cart.objects.create(total=0)
            self.request.session['cart_id']=cart_obj.id
            cartproduct=CartProduct.objects.create(cart=cart_obj,product=product_obj,rate=product_obj.selling_price,quantity=1,subtotal=subtotal)
            cart_obj.total=cartproduct.subtotal
            cart_obj.save()
        return redirect('mycart')
    


class ManageCartView(EcomMixin,View):
    def get(self, request, *args, **kwargs):
        cartprod_id=self.kwargs["id"]
        print(cartprod_id)
        cartprod_obj=CartProduct.objects.get(id=cartprod_id)
        cart_obj=cartprod_obj.cart
        action=self.request.GET['action']

        if action=="inc":
            cartprod_obj.quantity+=1
            cartprod_obj.subtotal+=cartprod_obj.rate
            cartprod_obj.save()
            cart_obj.total+=cartprod_obj.rate
            cart_obj.save()

        if action=="dsc":
            cartprod_obj.quantity-=1
            cartprod_obj.subtotal-=cartprod_obj.rate
            cartprod_obj.save()
            cart_obj.total-=cartprod_obj.rate
            cart_obj.save()

        if action=="rmv":
            cart_obj.total-=cartprod_obj.subtotal
            cart_obj.save()
            cartprod_obj.delete()


        return redirect('mycart')
    


class MyCart(EcomMixin,CartMixin,TemplateView):
    template_name="coza/shoping-cart.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cart_id=self.request.session.get("cart_id",None)
        if cart_id:
            cart=Cart.objects.get(id=cart_id)
        else:
            cart=None
        context['cart']=cart
        return context





class CheckOutView(EcomMixin,CartMixin,CreateView):
    template_name="coza/checkout.html"
    model=Order
    form_class=CheckOutForm
    success_url=reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/ecommerce/customer-login/?next=/ecommerce/checkout/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        cart_id=self.request.session.get("cart_id",None)
        if cart_id:
            cart_obj=Cart.objects.get(id=cart_id)
            form.instance.cart=cart_obj
            form.instance.ordered_by=self.request.user.customer
            form.instance.subtotal=cart_obj.total
            form.instance.discount=0
            form.instance.total=cart_obj.total
            del self.request.session['cart_id']
            form.save()
        else:
            return redirect("home")
        return super().form_valid(form)


class CustomerRegistration(CartMixin,CreateView):
    template_name="coza/customer_registration.html"
    model=Customer
    form_class=CustomerRegistrationForm
    success_url=reverse_lazy('home')

    def get_success_url(self):
        if "next" in self.request.GET:
            url=self.request.GET.get("next")
            return url
        return self.success_url

    def form_valid(self, form):
        username=form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        user=User.objects.create_user(username=username,email=email,password=password)
        print(user)
        form.instance.user=user
        login(self.request,user)
        return super().form_valid(form)

class CustomerLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')


class CustomerLoginView(FormView):
    template_name="useradmin/login.html"
    form_class=LoginForm
    success_url=reverse_lazy("home")

    def get_success_url(self):
        if "next" in self.request.GET:
            url=self.request.GET.get("next")
            print(url)
            return url
        return self.success_url

    def form_valid(self, form):
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        print("hello World")
        user=authenticate(username=username,password=password)
        if user is not None and User.objects.filter(username=user).exists():
            login(self.request,user)
        else:
            return render(self.request,self.template_name,{"form":self.form_class,"error":"Invalid Credintials"})
        return super().form_valid(form)









################################################################################################
###################################### For Review ##############################################

class ReviewCreateView(CreateView):
    success_url=reverse_lazy("home")
    model=CustomerReview
    fields=['product','rating','review','name','email']

    # def form_valid(self, form):
    #     product_id=form.cleaned_data['product_id']
    #     product=Product.objects.get(id=product_id)
    #     form.instance.product=product
    #     form.save()
    #     print(product_id)
    #     return super().form_valid(form)


class AdminReview(AdminMixin,ListView):
    template_name="useradmin/review.html"
    model=CustomerReview
    context_object_name="reviews"


class AdminReviewDelete(AdminMixin,DeleteView):
    model=CustomerReview
    success_url=reverse_lazy("admin-review")

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"Review Deleted Successfully !!!")
        return super().post(request, *args, **kwargs)