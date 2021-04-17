from django.shortcuts import render, Http404, get_object_or_404
from .models import Product, ProductImage, Category, School

# Create your views here.


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__startswith=q)
        context = {'query': q, 'products': products}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
    return render(request, template, context)



def home(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        images = product.productimage_set.all() #kyuki product Product ka instance hai na
        context = {'product': product, 'images': images}
        template = 'products/single.html'

    except:
        raise Http404

    return render(request, template, context)


# def filter(request):
#     categories = Category.objects.all()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products();
#
#     data = {}
#     data['products'] = products
#     data['categories'] = categories


# def menu_categories(request):
#     categories = Category.objects.filter(parent=None)
#     return {"menu_categories": categories}
#
#
# def category_detail(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     products = category.products.filter(parent=None)
#
#     context = {
#         'category': category,
#         'products': products
#     }
#
#     return render(request, 'category_detail.html', context)



def allSchools(request):
    schools = School.objects.all()
    context = {'schools': schools}
    template = 'products/allschools.html'
    return render(request, template, context)
