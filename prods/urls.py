from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('base', base, name='base'),
    path('home', home, name='home'),
    path('product',products_fun,name='product'),
    path('add/product',add_product,name = 'add_product'),
    path('delete/product/<int:id>',delete_product,name = 'delete_product'),    
    path('update/product/<int:id>',update_product,name = 'update_product'),
    path('category',category,name='category'),
    path('add/category',add_category,name='add_category'),
    path('delete/category/<int:id>',delete_category,name = 'delete_category'),
    path('update/category/<int:id>',update_category,name = 'update_category'),
    ####################################################################################################
    path('profile',profile,name = 'profile'),
    path('search',search_fun,name = 'search_fun'),#/<the_keyword>
    path('product_view',product_view.as_view(),name='product_view'),
#    path('checkboxes',checkboxes,name='checkboxes1'),
#    path('filer/<teto>',filer,name='filer1'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)