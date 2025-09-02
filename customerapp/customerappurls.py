from django.urls import path
from .import views
urlpatterns =[
    path('customerdash/',views.customerdash,name='customerdash'),
    path('customerlogout/',views.customerlogout,name='customerlogout'),
    path('customerproducts/',views.customerproducts,name='customerproducts'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('submitresponse/',views.submitresponse,name='submitresponse'),
]