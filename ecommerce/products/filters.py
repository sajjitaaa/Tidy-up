import django_filters
from .models import Product, School
from django import forms


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Product
        fields = ['title']
        widgets = {
         'title': forms.Select(attrs={'id':'choicewa'}),
         }


class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ['name']

class Sort_by_name_Filter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['title']
        widgets = {
         'title': forms.Select(attrs={'id':'choicewa'}),
         }

class Sort_by_price_Filter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['title']
        widgets = {
         'title': forms.Select(attrs={'id':'choicewa'}),
         }
