from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('', views.customers, name='customers'),
path('listingcustomers/', views.list_customers, name='listingcustomers'),
path('editcustomer/<str:pk>', views.edit_customer, name='editcustomer'),
path('deletecustomer/<str:pk>', views.delete_customers, name='deletecustomer'),
path('newsoftware/<str:pk>', views.new_software, name='software'),
path('softwarelist/', views.listsoftware, name='listingsoftware'),
path('deletesoftware/<str:pk>', views.delete_software, name='deletesoftware'),
path('editsoftware/<str:pk>', views.edit_software, name='editsoftware'),
path('customersoftware/<str:pk>', views.list_customer_software, name='customersoftware'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)