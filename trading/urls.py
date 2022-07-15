from django.urls import path 
from . import views 

urlpatterns =[
    path('login',views.loginPage,name ='login'),
    path('',views.home, name = 'home'),
    path('profile' , views.createProfile,name = 'profile-CU'),
    path('new_product',views.postProduct,name ='post-product'),
    path('logout',views.signOut,name = 'logout'),
    path('register',views.createUser, name = 'register'),
    path('checkup/<str:pk>',views.profile_page,name ='profile-page'),
    path('product-page/<str:pk>',views.checkProduct,name = 'product-page'),
    path('contact-form',views.edit_contactInfo, name='contact-form'),
    path('pay/<str:pk>',views.pay, name ='payment')
]
