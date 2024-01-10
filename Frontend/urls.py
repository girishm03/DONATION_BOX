from django.urls import path
from Frontend import views

urlpatterns = [
    # User login and signup page
    path('register_page/', views.register_page, name='register_page'),
    path('UserLogin/', views.UserLogin, name='UserLogin'),
    path('User_logout/', views.User_logout, name='User_logout'),
    # Website contents
    path('Homepage/', views.Homepage, name='Homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Camp/', views.Camp, name='Camp'),
    path('donate/', views.donate, name='donate'),
    path('blog/', views.blog, name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    # Website Data
    path('registerdata/', views.registerdata, name='registerdata'),
    path('contibdata/', views.contibdata, name='contibdata'),
    path('itemdata/', views.itemdata, name='itemdata'),
]
