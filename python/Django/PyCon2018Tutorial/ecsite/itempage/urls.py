from django.conf.urls import url
from django.shortcuts import render
from itempage import views

urlpatterns = [
    url(r'^item/(?P<item_id>\d+)/$', views.item_page_display),
    url(r'^item_search$', views.item_search),
    url(r'^add_to_cart', views.add_to_cart, name='add_to_cart'),
    url(r'^cart', views.cart_display, name='cart_display'),
    url(r'^order_form$', views.order_form, name="order_form"),
    url(r'^complete$', render, {
        'template_name': 'complete.html'}, name='complete'),
]
