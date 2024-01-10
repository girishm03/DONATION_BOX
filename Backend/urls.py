from django.urls import path
from Backend import views

urlpatterns = [
    # Admin side login
    path('admin_login/', views.admin_login, name='admin_login'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    # index page
    path('INDEX/', views.INDEX, name='INDEX'),
    # Front-end datas
    path('Users/', views.Users, name='Users'),
    path('items/', views.items, name='items'),
    path('contribution/', views.contribution, name='contribution'),
    # Category - add, display, update and delete
    path('Category/', views.Category, name='Category'),
    path('cdata/', views.cdata, name='cdata'),
    path('displaycat/', views.displaycat, name='displaycat'),
    path('Editcat/<int:dataid>/', views.Editcat, name='Editcat'),
    path('updatecategory/<int:dataid>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:dataid>/', views.deletecategory, name='deletecategory'),
    # Website link - add, display, update and delete
    path('weblink/', views.weblink, name='weblink'),
    path('wdata/', views.wdata, name='wdata'),
    path('displayWeb/', views.displayWeb, name='displayWeb'),
    path('EditWeb/<int:dataid>/', views.EditWeb, name='EditWeb'),
    path('updateWeb/<int:dataid>/', views.updateWeb, name='updateWeb'),
    path('deleteWeb/<int:dataid>/', views.deleteWeb, name='deleteWeb'),
    # Donor/Volunteer - add, display, update and delete
    path('Person_DV/', views.Person_DV, name='Person_DV'),
    path('pdata/', views.pdata, name='pdata'),
    path('displayper/', views.displayper, name='displayper'),
    path('Editper/<int:dataid>/', views.Editper, name='Editper'),
    path('updateper/<int:dataid>/', views.updateper, name='updateper'),
    path('deleteper/<int:dataid>/', views.deleteper, name='deleteper'),
]