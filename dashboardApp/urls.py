from django.urls import path
from dashboardApp.views import *

from . import views


app_name = 'dashboardApp'

urlpatterns = [

 	path('admindashboard',views.Dashboard.as_view(),name = 'admindashboard'),
    path('dashboardlogin',views.DashboardLogin.as_view(),name = 'dashboardlogin'),
    path('logout',views.AdminLogout.as_view(),name = 'logout'),
    # path('add_items/<num>',views.AddProducts.as_view(),name = 'add_items'),

    path('add_items',views.AddProducts.as_view(),name = 'add_items'),

    path('all_products',views.AllProducts.as_view(),name = 'all_products'),
    path('deletedata',views.DeleteData.as_view(),name = 'deletedata'),
    path('edit_product',views.EditProduct.as_view(),name = 'edit_product'),


]