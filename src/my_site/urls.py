'''
Created on Nov 8, 2017

@author: Que Huong
'''
from django.conf.urls import url
from my_site import views

urlpatterns = [
    url(r'^index.html/$', views.index, name='index'),
    url(r'^products.html/$', views.products, name='products'),
    url(r'^single.html/$', views.single, name='single'),
    url(r'^contact.html/$', views.contact, name='contact'),
    url(r'^login.html/$', views.login, name='login'),
    url(r'^registered.html/$', views.registered, name='registered'),
    url(r'^faq.html/$', views.faq, name='faq'),
]