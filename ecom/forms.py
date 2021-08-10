from .models import Banner,Category,Product,ProductImages,Order,Customer
from django import forms
from django.contrib.auth.models import User


class CustomerRegistrationForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Customer
        fields=['fullname','address']
        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }




class BannerForm(forms.ModelForm):
    class Meta:
        model=Banner
        fields='__all__'
        # fields=['title','image','link','status','added_by']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'added_by':forms.Select(attrs={'class':'form-control'}),
        }

        error_messages = {
            'title': {
                'required': "Title is Required"
            },
            'image':{
                'required':'Image field is required'
            },
            'status':{
                'required':'Status Field is Required'
            },
            'added_by':{
                'required':'Added By Field is required'
            }
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['title','is_parent','status','parent_id','image']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'is_parent':forms.CheckboxInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'parent_id':forms.Select(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

        error_messages={
            'title':{'required':'Title is Required'},
            'status':{'required':'Status is Requiered'},
            'image':{'required':'Image Field is Required'},
        }

class ProductForm(forms.ModelForm):
    more_images=forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple':True}))
    class Meta:
        model=Product
        fields=['title','slug','category','image','status','marked_price','selling_price','description','warrenty','return_policy']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'marked_price':forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'warrenty':forms.TextInput(attrs={'class':'form-control'}),
            'return_policy':forms.TextInput(attrs={'class':'form-control'}),
        }

        error_messages={
            'title':{'required':'Title is Required'},
            'slug':{'required':'Slug Field is Required'},
            'category':{'required':'Category Field is Required'},
            'image':{'required':'Image Field is Required'},
            'status':{'required':'Status is Requiered'},
            'marked_price':{'required':'Marked Price is Required'},
            'selling_price':{'required':'Selling Price is Required'},
        }




class CheckOutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['shipping_address','mobile','email']

        widgets={
            'shipping_address':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    


class AdminOrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['discount','order_status']

        widgets={
            'discount':forms.NumberInput(attrs={'class':'form-control'}),
            'order_status':forms.Select(attrs={'class':'form-control'}),
        }