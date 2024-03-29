from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path("",views.login, name='login'),
    path('login/', views.login, name='login'), 
    path('welcome/', views.welcome, name='welcome'),     
    path('register/', views.register, name='register'), 
    path('thankyou/', views.thankyou, name='thankyou'),  
    path("main/",views.main, name='login'),
    path("users/",views.users,name="users"),
    path('useraccount/', views.useraccount, name='useraccount'),  
    path("userdetails/<slug>",views.user,name="users"),
    path("delete_user/<int:id>",views.delete_user,name="delete_user"),
    path("category/",views.category,name="category"),
    path("delete_category/<int:id>",views.delete_category,name="delete_category"),
    path("suppliers/",views.suppliers,name="suppliers"),
    path("show_suppliers/<int:id>",views.show_suppliers,name="show_suppliers"),
    path("delete_supplier/<int:id>",views.delete_supplier,name="delete_supplier"),
    path("products/",views.products,name="products"),
    path("search_product/",views.search_product,name="search_product"),
    path("products/<int:id>",views.show,name="show"),
    path('delete_product/<int:id>', views.delete_pro, name='delete_pro'),
    path('testing/', views.testing, name='testing'),  
    path('sales/', views.sales, name='sales'), 
    path('customerbill/', views.customer_bill, name='customerbill'), 
    path('show_product_customerbill/<int:id>', views.show_product_customerbill, name='show_product_customerbill'), 
    path('addupdatecart/', views.add_update_cart, name='addupdatecart'), 
    path('delete_cartitem/<int:id>', views.delete_cartitem, name='delete_cartitem'), 
    path('clear_cart/', views.clear_cart, name='clear_cart'), 
    path('generate_bill/', views.generate_bill, name='generate_bill'), 
    path('print_bill/', views.print_bill, name='print_bill'), 
    path('jasondata/', views.jasondata, name='jasondata'), 
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
