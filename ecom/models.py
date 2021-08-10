from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suscribe(models.Model):
    email=models.EmailField(max_length=50)

class ContactUs(models.Model):
    email=models.EmailField(max_length=50)
    msg=models.CharField(max_length=700)



class UserImage(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="profile_pic")


    def delete(self, using=None, keep_parents=False):
        self.image.delete(self.image.name)
        return super().delete(using=using, keep_parents=keep_parents)

    def save(self,*args,**kwargs):
        try:
            this=UserImage.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()

        except:
            pass
        super(UserImage,self).save(*args,**kwargs)





class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=50)
    address=models.CharField(max_length=50,null=True,blank=True)
    joined_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname




class Banner(models.Model):
    title=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=[('active','Active'),('inactive','In Active')])
    image=models.ImageField(upload_to="banners")
    added_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def save(self, *args, **kwargs):
        try:
            this = Banner.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: 
            pass
        super(Banner, self).save(*args, **kwargs)


class Category(models.Model):
    title=models.CharField(max_length=40)
    is_parent=models.BooleanField(default=True)
    image=models.ImageField(upload_to='categories')
    parent_id=models.ForeignKey('self',on_delete=models.CASCADE,default=None,blank=True,null=True)
    status=models.CharField(max_length=30,choices=[('active','Active'),('inactive','In Active')])
    
    def __str__(self):
        return self.title

    def delete(self,using=None,keep_parents=False):
        products=Product.objects.filter(category=self.id)
        for product in products:
            more_images=ProductImages.objects.filter(product=product.id)
            for mi in more_images:
                mi.image.storage.delete(mi.image.name)
            product.image.storage.delete(product.image.name)
        self.image.storage.delete(self.image.name)
        super().delete()


    def save(self,*args,**kwargs):
        try:
            this=self.Category.objects.get(id=self.id)
            if this.image!=self.image:
                this.image.delete()
        except:
            pass
        super(Category,self).save(*args,**kwargs)


class Product(models.Model):
    title=models.CharField(max_length=70)
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="products")
    status=models.CharField(max_length=10,choices=[('Active','Active'),('In Active','In Active')],default="Active")
    marked_price=models.PositiveIntegerField()
    selling_price=models.PositiveIntegerField()
    description=models.TextField()
    warrenty=models.CharField(max_length=300,null=True,blank=True)
    return_policy=models.CharField(max_length=200,null=True,blank=True)
    view_count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        more_images=ProductImages.objects.filter(product=self.id)
        for mi in more_images:
            mi.image.storage.delete(mi.image.name)
        self.image.storage.delete(self.image.name)
        super().delete()

    def save(self,*args,**kwargs):
        try:
            this=self.Product.objects.get(id=self.id)
            if this.image!=self.image:
                this.image.delete()
        except:
            pass
        super(Product,self).save(*args,**kwargs)

    
class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="more_images")
    image=models.ImageField(upload_to="productimages")

    def __str__(self):
        return self.product.title



class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    total=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: "+str(self.id)

class CartProduct(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    rate=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    subtotal=models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return "Cart "+str(self.cart.id)+"Product "+str(self.id)


ORDER_STATUS=(
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("On The Way","On The Way"),
    ("Order Completed","Order Completed"),
    ("Order Cancled","Order Cancled"),
)
class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by=models.ForeignKey(Customer,on_delete=models.CASCADE)
    shipping_address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(max_length=50,null=True,blank=True)
    subtotal=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    order_status=models.CharField(max_length=50,choices=ORDER_STATUS,default="On The Way")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Order : "+str(self.id)

class CustomerReview(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField()
    review=models.CharField(max_length=500)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return "Reviewed By "+str(self.name)