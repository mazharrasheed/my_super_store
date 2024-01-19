from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from .models import Members,Users,Products,Category,Suppliers,Cart,Sales
from .forms import Userform ,RegisterUser,LoginUser,Products_form,Category_form,Suppliers_form,Search_product_form,Customer_detail_form,Cust_bill_Products_form
import time
import os
import tempfile
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.

def main(request):

    mycategory = Category.objects.filter(is_deleted=False).values()
    myproducts = Products.objects.filter(is_deleted=False).values()
    mysuppliers = Suppliers.objects.filter(is_deleted=False).values()
    mysales = Sales.objects.all().values()
    myusers = Users.objects.filter(is_deleted=False).values()
    data={'mycategory':mycategory,'myproducts':myproducts,'mysuppliers':mysuppliers,'myusers':myusers,'mysales':mysales}
    template=loader.get_template('main.html') # this will not work when we use POST method
    return HttpResponse(template.render(data))    # this will not work when we use POST method

def users(request):
    myusers = Users.objects.filter(is_deleted=False).values()
    paginator=Paginator(myusers,1)
    page_num=request.GET.get("page")
    myusersfinal=paginator.get_page(page_num)
    totalpages=myusersfinal.paginator.num_pages
    template=loader.get_template('users.html')
    context= {'myusers':myusersfinal,"lastpage":totalpages,"pagelist":[n+1 for n in range(totalpages)]}
    return HttpResponse(template.render(context))

def user(request,slug):
    details=True
    myusers = Users.objects.filter(user_slug=slug)
    template=loader.get_template('users.html')
    context= {'myusers':myusers,'details':details}
    return HttpResponse(template.render(context))

def delete_user(request,id):
    myusers = Users.objects.get(id=id)
    myusers.is_deleted=True
    myusers.save()
    template=loader.get_template('users.html')
    url="/users/"
    return HttpResponseRedirect(url) 

def register(request):
  error=False
  username=""
  try:
      if request.method == 'POST':
        form = RegisterUser(request.POST) # Return form to html and also input data to form.
        username=request.POST.get('username')
        password=request.POST.get('password')
        allusers=Users.objects.all().values()
        for entry in allusers:
          if username==entry['username']:
            error=True
            break
        else:
          users=Users(username=username,password=password)
          users.save()
          url="/welcome/?output={}".format(str(username).capitalize()) 
          return HttpResponseRedirect(url) # Redirect to Welcome you page with some data.
      else:
          form = RegisterUser()
  except:
          pass
  data={'form':form ,'error':error}
  return render(request,'register.html',data)

def login(request):

  error=False
  form = RegisterUser()
  try:
      if request.method == 'POST':
        form = LoginUser(request.POST) # Return form to html and also input data to form.
        username=request.POST.get('username')
        password=request.POST.get('password')
        allusers=Users.objects.all().values()
        for entry in allusers:
          if username==entry['username'] and password==entry['password']:
            url="/useraccount/?output={}".format(str(username).capitalize()) 
            return HttpResponseRedirect(url) # Redirect to Welcome you page with some data .
          else:
            error=True
      else:
          form = LoginUser()
  except:
          pass
  data={'form':form,'error': error}
  return render(request,'login.html',data)

def category(request):
    error=False
    msg=False
    try:
      if request.method == 'POST':
        form =Category_form() # Return form to html
        category_name=str(request.POST.get('category_name')).capitalize()
        allcategory=Category.objects.filter(is_deleted=False).values()
        for entry in allcategory:
          if category_name==entry['category_name']:
            error=True
            break
        else:
            prod=Category(category_name=category_name)
            prod.save()
            msg=True
      else:
        form=Category_form()
    except:
            pass
    mycategory = Category.objects.filter(is_deleted=False).values()
    data={'form':form ,'error':error,'mycategory':mycategory,'msg':msg }
    return render(request,'category.html',data)

def delete_category(request,id):
  cat=Category.objects.get(id=id)
  cat.is_deleted=True
  cat.save()
  url="/category/"
  return HttpResponseRedirect(url) 
  # return render(request,'products.html')

def products(request):
    error=False
    error1=False
    msg=False
    try:
        if request.method == 'POST':
          form =Products_form() # Return form to html
          category_name=str(request.POST.get('category_name')).capitalize()
          productname=str(request.POST.get('productname')).capitalize()
          product_perchase_price=str(request.POST.get('product_perchase_price')).capitalize()
          product_sale_price=str(request.POST.get('product_sale_price')).capitalize()
          product_quantity=(request.POST.get('product_quantity'))
          product_status=(request.POST.get('status'))

          allproducts=Products.objects.filter(is_deleted=False).values()

          if  category_name=="":
              error1=True
          else:
            for entry in allproducts:
              if productname==entry['productname']:
                error=True
                break
            else:
              prod=Products(productname=productname,product_perchase_price= product_perchase_price,product_sale_price=product_sale_price,category=category_name,product_quantity=product_quantity,product_status=product_status)
              prod.save()
              msg=True
        else:
            form = Products_form()
    except:
            pass
    mycategory = Category.objects.filter(is_deleted=False).values()
    myproducts = Products.objects.filter(is_deleted=False).values()
    data={'form':form ,'error':error,'error1':error1,'myproducts':myproducts,'mycategory':mycategory,'msg':msg }
    return render(request,'products.html',data)

def show(request,id):
    error1=False
    error=False
    msg=False
    # myproduc = Products.objects.get(id=id)
    try:
        if request.method == 'POST':
          form =Products_form(request.POST) # Return form to html and also input data to form.
          category_name=str(request.POST.get('category_name')).capitalize()
          productname=str(request.POST.get('productname')).capitalize()
          product_perchase_price=str(request.POST.get('product_perchase_price')).capitalize()
          product_sale_price=str(request.POST.get('product_sale_price')).capitalize()
          product_quantity=(request.POST.get('product_quantity'))
          product_status=(request.POST.get('status'))
          rows_affected = Products.objects.select_for_update().filter(id=id, is_deleted=False).update(productname=productname,product_perchase_price= product_perchase_price,product_sale_price=product_sale_price,category=category_name,product_quantity=product_quantity,product_status=product_status)
          if rows_affected == 0:
             error=True
          else: 
             msg=True
          data = {'error':error,'msg':msg}
          return redirect('products', data)              
        else:
            form = Products_form()
    except:
            pass
    mycategory = Category.objects.filter(is_deleted=False).values()
    mydata = Products.objects.filter(id=id, is_deleted=False).values()
    print(mydata)
    for x in mydata:
      value1=x['category']
      value2=x['productname']
      value3=x['product_perchase_price']
      value4=x['product_sale_price']
      value5=x['product_quantity']
      value6=x['product_status']

    form.fields['productname'].widget.attrs['value'] = value2
    form.fields['product_perchase_price'].widget.attrs['value'] = value3
    form.fields['product_sale_price'].widget.attrs['value'] = value4
    form.fields['product_quantity'].widget.attrs['value'] = value5

    data={'form':form ,'myproducts':mydata,'error':error,'msg':msg,'error1':error1,'mycategory':mycategory,'value1':value1,'value6':value6, 'update_mode': True }
    return render(request,'products.html',data)

def search_product(request):
    s_error=False
    search_p=""
    try:
        if request.method == 'POST':
          search_name=str((request.POST.get('search'))).capitalize()
          if search_name=="":
             s_error=True
          else:
              search_p = Products.objects.filter(productname__icontains=search_name, is_deleted=False).values()     
    except:
       pass
    form =Products_form() # Return form to html.
    data={'myproducts':search_p,'s_error':s_error, 'search_mode':True}
    return render(request,'products.html',data)

def delete_pro(request,id):
  pro=Products.objects.get(id=id)
  pro.is_deleted=True
  pro.save()
  url="/products/"
  return HttpResponseRedirect(url) # Redirect to Welcome you page with some data .
  # return render(request,'products.html')

def details(request,id):
  myproducts = Products.objects.get(id=id)
  template = loader.get_template('pupdate.html') # this will not work when we use POsT method (csrf token not generated)
  context = {'myproducts': myproducts,}
  return HttpResponse(template.render(context))  # this will not work when we use POST method

def contactus(request):

  # try:
  #     if request.method=='get':
  #       fname=request.GET['ftname']
  #       lname=request.GET['ltname']

  #       fname=request.GET.get('ftname')
  #       lname=request.GET.get('ltname')
  #       fullname=(fname+" "+lname)
  #       context={"var1":fullname}
  # except:
  #   pass

    context={}

    try:
        if request.method == 'POST':
          fname=request.POST.get('firstname')
          lname=request.POST.get('lastname')
          lname=str(lname).lower().capitalize()
          fname=str(fname).lower().capitalize()
          context={'var1':fname, 'var2':lname}
          url="/thankyou/?output={} {}".format(fname,lname)  
          return HttpResponseRedirect(url) # Redirect to thanks you page with some data .
          # return redirect(url) # Redirect to thanks you page with some data . 
    except:
          pass
    return render(request,'contactus.html',context) # when we use form get method this method will work

def thankyou(request):
  if request.method=='GET':
    output=request.GET.get('output')
  return render(request,'thankyou.html',{'output':output})

def welcome(request):
  if request.method=='GET':
    output=request.GET.get('output')
  return render(request,'welcome.html',{'output':output})

def useraccount(request):
  if request.method=='GET':
    output=request.GET.get('output')
  return render(request,'useraccount.html',{'output':output})


def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry','Mango','Kivee'],   
  }
  return HttpResponse(template.render(context, request))

def testing1(request):
  mydata=Members.objects.all().values()
  mydata3=Members.objects.values_list('firstname')
  mydata1=[]
  for x in mydata3:
    mydata1.append(x[0])

  mydata2=Members.objects.filter(firstname='Mazhar').values()
  template = loader.get_template('template123.html')
  context = {
    'mymembers': mydata ,'col': mydata1 ,'row': mydata2
  }
  return HttpResponse(template.render(context,request))  

def suppliers(request):
    error=False
    error1=False
    msg=False
    try:
        if request.method == 'POST':
          form =Suppliers_form()  # Return form to html
          firstname=str(request.POST.get('firstname')).capitalize()
          lastname=str(request.POST.get('lastname')).capitalize()
          contact=str(request.POST.get('contact')).capitalize()
          adress=str(request.POST.get('adress')).capitalize()
          description=str(request.POST.get('description')).capitalize()
          allsuppliers=Suppliers.objects.filter(is_deleted=False).values()
          for entry in allsuppliers:
            if firstname==entry['firstname'] :
              error=True
              break
          else:
            Supps=Suppliers(firstname=firstname,lastname=lastname,contact=contact,adress=adress,description=description,)
            Supps.save()
            msg=True
        else:
            form = Suppliers_form()
    except:
            pass
    mysuppliers = Suppliers.objects.filter(is_deleted=False).values()
    data={'form':form ,'error':error,'error1':error1,'mysuppliers':mysuppliers,'msg':msg }
    return render(request,'suppliers.html',data)

def show_suppliers(request,id):
    error=False
    error1=False
    msg=False
    update_mode=True
    try:
        if request.method == 'POST':
          form =Suppliers_form()  # Return form to html
          firstname=str(request.POST.get('firstname')).capitalize()
          lastname=str(request.POST.get('lastname')).capitalize()
          contact=str(request.POST.get('contact')).capitalize()
          adress=str(request.POST.get('adress')).capitalize()
          description=str(request.POST.get('description')).capitalize()

          # allsuppliers=Suppliers.objects.select_for_update.get(id=id)
          rows_affected = Suppliers.objects.select_for_update().filter(id=id, is_deleted=False).update(firstname=firstname,lastname=lastname,contact=contact,adress=adress,description=description,)
          if rows_affected == 0:
             error=True
          else: 
             msg=True
          data = {'error':error,'msg':msg}
          return redirect('suppliers', data)

        else:
            form = Suppliers_form()
    except:
            pass

    mydata = Suppliers.objects.filter(id=id).values()
    for x in mydata:
      value1=x['firstname']
      value2=x['lastname']
      value3=x['contact']
      value4=x['adress']
      value5=x['description']

    form.fields['firstname'].widget.attrs['value'] = value1
    form.fields['lastname'].widget.attrs['value'] = value2
    form.fields['contact'].widget.attrs['value'] = value3
    form.fields['adress'].widget.attrs['value'] = value4
    form.fields['description'].widget.attrs['value'] = value5
    data={'form':form ,'mysuppliers':mydata,'msg':msg ,'update_mode':update_mode}
    return render(request,'suppliers.html',data)

def delete_supplier(request,id):
  supp=Suppliers.objects.get(id=id)
  supp.is_deleted=True
  supp.save()
  url="/suppliers/"
  return HttpResponseRedirect(url)

def sales(request):

  mysales = Sales.objects.all().values()
   
  data={'mysales':mysales}
   
  return render(request,'sales.html',data)
   

def customer_bill(request):
   
    error=False
    error1=False
    msg=False
    try:
        if request.method == 'POST':
          search_form=Search_product_form()
          cust_form=Customer_detail_form()
          form =Cust_bill_Products_form() # Return form to html

          productname=str(request.POST.get('productname')).capitalize()
          product_sale_price=str(request.POST.get('product_sale_price')).capitalize()
          product_quantity=(request.POST.get('product_quantity'))
          product_status=(request.POST.get('status'))

        else:
            form = Cust_bill_Products_form()
            search_form=Search_product_form()
            cust_form=Customer_detail_form()
    except:
            pass
    clear_cart(request)
    mycategory = Category.objects.filter(is_deleted=False).values()
    myproducts = Products.objects.filter(is_deleted=False,product_status="active").values()
    cartitems=Cart.objects.filter(is_deleted=False).values()  
    data={'form':form,'search_form':search_form ,'cartitems':cartitems,'cust_form':cust_form,'error':error,'error1':error1,'myproducts':myproducts,'mycategory':mycategory,'msg':msg }
    return render(request,'customerbill.html',data)
   
def show_product_customerbill(request,id):
    error1=False
    error=False
    msg=False
    id=int(id)
    # myproduc = Products.objects.get(id=id)
    try:
        if request.method == 'POST':
            cust_form=Customer_detail_form()
            form =Cust_bill_Products_form(request.POST) # Return form to html and also input data to form.
            search_form=Search_product_form()
                         
        else:
            form = Cust_bill_Products_form()
            search_form=Search_product_form()
            cust_form=Customer_detail_form()
    except:
            pass
    mycategory = Category.objects.filter(is_deleted=False).values()
    mydata1 = Products.objects.filter(is_deleted=False,product_status="active").values()
    mydata = Products.objects.filter(id=id, is_deleted=False).values()
    cartitems=Cart.objects.filter(is_deleted=False).values()  
    for x in mydata:
      value2=x['productname']
      value5=x['product_quantity']

    data={'form':form ,'search_form':search_form ,'cartitems':cartitems,'cust_form':cust_form,'myproducts':mydata1,'error':error,'msg':msg,'error1':error1,'mycategory':mycategory,'value2':value2,'value5':value5, 'show_mode': True }
    return render(request,'customerbill.html',data)
  
def add_update_cart(request):

  error1=False
  error2=False
  try:
    if request.method == 'POST':
      cust_form=Customer_detail_form()
      search_form=Search_product_form()
      productname=request.POST.get('all_products')
      product_quantity =request.POST.get('proqty') 

      cartitem=Products.objects.filter(productname=productname, is_deleted=False, product_status='active')  
      for x in cartitem:
        pid=x.id
        productname=x.productname
        product_sale_price=float(x.product_sale_price)
        product_quantity=int(product_quantity)
        is_deleted=False
        in_stock=x.product_quantity
        if product_quantity >int( x.product_quantity):
           error1=True
        else:
          total_price=float(product_quantity*product_sale_price)   
      citem=Cart(pid=pid,productname=productname,product_sale_price=product_sale_price,
      product_quantity=product_quantity,total_price=total_price,is_deleted=is_deleted,in_stock=in_stock)

      present=False
      cartlist=Cart.objects.filter(productname=productname)
      for item in cartlist:
         if productname==item.productname:
            present=True
            break
      if present==True:
            error2=True
      else:
          citem.save()
    else:
      search_form=Search_product_form() 
      cust_form=Customer_detail_form()        
  except:
     pass 
  myproducts = Products.objects.filter(is_deleted=False,product_status="active").values()
  cartitems=Cart.objects.filter(is_deleted=False).values()  

  bill_amnt=0
  net_pay=0
  discount=0

  for item in cartitems:
    bill_amnt=bill_amnt+float(item['total_price'])
    discount=(bill_amnt*5)/100
    net_pay=bill_amnt-((bill_amnt*5)/100)
  data={'search_form':search_form ,'cartitems':cartitems ,'myproducts':myproducts,'cust_form':cust_form,'bill_amnt':bill_amnt,'discount':discount,'net_pay': net_pay,'error1':error1,'error2':error2}
  return render(request,'customerbill.html',data)

def delete_cartitem(request,id):
  item=Cart.objects.filter(id=id).delete()
  # item.is_deleted=True
  # item.save()
  url="/addupdatecart"
  return HttpResponseRedirect(url)

def clear_cart(request):
  item=Cart.objects.all().delete()
  # item.is_deleted=True
  # item.save()
  url="/customerbill"
  return HttpResponseRedirect(url)

def generate_bill(request):
   
  try:
      
    if request.method=='POST':

      search_form=Search_product_form()
      cust_form=Customer_detail_form(request.POST)
      customer_name=request.POST.get('customer_name') 
      customer_contact=request.POST.get('customer_contact') 
      
    else:
        search_form=Search_product_form() 
        cust_form=Customer_detail_form()
  except:
    pass

  cartitems=Cart.objects.filter(is_deleted=False).values()  

  for item in cartitems:
    id=item['pid']
    qty=int(item['in_stock'])-int(item['product_quantity'])
    if int(item['product_quantity'])==int(item['in_stock']):
      status="inactive"
    if int(item['product_quantity'])!=int(item['in_stock']):
      status="active"
    Products.objects.select_for_update().filter(id=id, is_deleted=False).update(product_quantity=qty,product_status=status)

  bill_amnt=0
  net_pay=0
  for item in cartitems:       
    bill_amnt=bill_amnt+float(item['total_price'])
    discount=(bill_amnt*5)/100
    net_pay=bill_amnt-((bill_amnt*5)/100)
# bill_top 
  global invoice
  invoice= int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
  bill_top=f'''
\t\tXYZ- Inventory
Phone No. 98725***** ,      Gujranwla-25250
{str("=")*52}
Customer Name  : {customer_name}
Ph.No : {customer_contact}
Bill No. {str(invoice)}\t Date : {str(time.strftime("%d//%m//%Y"))}
{str("=")*52}
                '''
# bill_Middle
  cartitems=Cart.objects.filter(is_deleted=False).values() 
# bill_bottom
  bill_bottom_temp=f'''
{str("=")*52}
Bill Amount\t\tRs. {bill_amnt},
Discount\t\tRs. {discount},
Net Pay\t\t\tRs. {net_pay},
{str("=")*52} '''
 
  myproducts = Products.objects.filter(is_deleted=False,product_status="active").values()
  cartitems=Cart.objects.filter(is_deleted=False).values()  
  data={'generate':True,'search_form':search_form ,'cartitems':cartitems ,'myproducts':myproducts,'cust_form':cust_form,'bill_top':bill_top,'bill_bottom_temp':bill_bottom_temp,'bill_amnt':bill_amnt,'discount':discount,'net_pay': net_pay}
  
  return render(request,'customerbill.html',data)

def print_bill(request):

  bill_amnt=0
  net_pay=0
  discount=0

  try:

    if request.method=='POST':
      text_area=request.POST.get('text_area')
      customer_name=request.POST.get('customer_name')
      customer_contact=request.POST.get('customer_contact') 
      sale=request.POST.get('text_area')

      cartitems=Cart.objects.filter(is_deleted=False).values()  
      for item in cartitems:
        bill_amnt=bill_amnt+float(item['total_price'])
        discount=(bill_amnt*5)/100
        net_pay=bill_amnt-((bill_amnt*5)/100)

      sales=Sales(bid=invoice, custname=customer_name,custcont=customer_contact,sale=sale,tamount= bill_amnt,disc=discount ,netpay=net_pay)
      sales.save()

  except:
    pass
  
  new_file=tempfile.mktemp('.txt')
  open(new_file,'w').write(text_area)
  os.startfile(new_file,'print')
  url="/customerbill"
  return HttpResponseRedirect(url)

def jasondata(request):
   
   data={
      
      'fname':'mazhar',
      'lname':'Rasheed',
   }

   return JsonResponse(data)