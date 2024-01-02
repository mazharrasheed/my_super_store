
from django import forms


class Userform(forms.Form):

    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=50)

    # num2=forms.EmailField(label='E-mail')

class RegisterUser(forms.Form):
    username=forms.CharField(max_length=50)
    # password=forms.CharField(max_length=20)
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'myfieldclass'}))

class LoginUser(forms.Form):
    username=forms.CharField(max_length=50)
    # password=forms.CharField(max_length=20)
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'myfieldclass'} ))

class Products_form(forms.Form):

    productname=forms.CharField(max_length=255)
    product_perchase_price=forms.CharField( max_length=255)
    product_sale_price=forms.CharField( max_length=255)
    product_quantity=forms.CharField( max_length=12)

class Products_update_form(forms.Form):
        
    productname=forms.CharField(widget=forms.TextInput(attrs={'value':""} ))
    product_perchase_price=forms.CharField(widget=forms.TextInput(attrs={'value':""} ))
    product_sale_price=forms.CharField(widget=forms.TextInput(attrs={'value':""} ))

class Category_form(forms.Form):
       
    category_name=forms.CharField(max_length=255)

class Suppliers_form(forms.Form):
    firstname=forms.CharField(max_length=255)
    lastname=forms.CharField(max_length=255)
    contact=forms.CharField(max_length=255)
 
    adress=forms.CharField(max_length=255)
    description=forms.CharField(max_length=255)

class Cust_bill_Products_form(forms.Form):

    productname=forms.CharField(max_length=255)
    product_sale_price=forms.CharField( max_length=255)
    product_quantity=forms.CharField( max_length=12)

class Search_product_form(forms.Form):
    search_product=forms.CharField(max_length=255)

class Customer_detail_form(forms.Form):
    customer_name=forms.CharField(max_length=255)
    customer_contact=forms.CharField(max_length=255)

