"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from products import views
from django.conf import settings
from django.conf.urls.static import static
from carts import views as cartviews
from orders import views as orderviews
from accounts import views as accountviews

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home',),
    url(r'^products/$', views.all, name='allproducts',),
    url(r'^products/(?P<slug>[\w-]+)/$', views.single, name="single"),
    url(r'^s/$', views.search, name='search',),
    url(r'^cart/$', cartviews.view, name='cart',),
    url(r'^cart/(?P<slug>[\w-]+)/$', cartviews.add_to_cart, name='add_to_cart'),
    url(r'^cart/(?P<id>\d+)/$', cartviews.remove_from_cart, name='remove_from_cart'),
    url(r'^checkout/$', orderviews.checkout, name='checkout',),
    url(r'^orders/$', orderviews.orders, name='user_orders',),
    url(r'^accounts/logout/$', accountviews.logout_view, name='auth_logout'),
    url(r'^accounts/login/$', accountviews.login_view, name='auth_login'),
    url(r'^accounts/register/$', accountviews.registration_view, name='auth_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
