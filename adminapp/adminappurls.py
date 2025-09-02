from django.urls import path
from .import views
urlpatterns =[
    path("admindash/",views.admindash,name='admindash'),
    path("adminlogout/",views.adminlogout,name='adminlogout'),
    path("viewenq/",views.viewenq,name='viewenq'),
    path("addproduct/",views.addproduct,name='addproduct'),
    path("viewproduct/",views.viewproduct,name='viewproduct'),
    path("delproduct/<int:pid>",views.delproduct,name='delproduct'),
    path("viewfeedbacks/",views.viewfeedbacks,name='viewfeedbacks'),
    path("viewcomplaints/",views.viewcomplaints,name='viewcomplaints'),
    path("delcomplaints/<int:id>",views.delcomplaints,name='delcomplaints'),
    path("delfeedbacks/<int:id>",views.delfeedbacks,name='delfeedbacks'),
]