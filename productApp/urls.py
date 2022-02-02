from django.urls import path

from . import views


app_name = 'productApp'

urlpatterns = [


    path('',views.HomePage.as_view(),name = 'home' ),
    path('signup',views.Signup.as_view(),name = 'signup'),
    path('login',views.Login.as_view(),name = 'login'),
    path('aboutus',views.AboutUs.as_view(),name = 'aboutus'),
    path('view_products',views.ViewProducts.as_view(),name = 'view_products'),
    path('product_page/<slug>',views.ProductDetailPage.as_view(),name = 'product_page'),
    path('user_logout',views.UserLogout.as_view(),name = 'user_logout'),
    path('forget_password',views.ForgetPassword.as_view(),name = 'forget_password'),
    path('reset_password/<str:verification_id>',views.ResetPassword.as_view(),name = 'reset_password'),
	






]