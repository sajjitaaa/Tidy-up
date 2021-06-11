from django.shortcuts import render, Http404, get_object_or_404
from .models import Product, ProductImage, Category, School
from .filters import ProductFilter, SchoolFilter, Sort_by_name_Filter, Sort_by_price_Filter
from django.db.models import Q
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


def all(request):
    products = Product.objects.all()
    schools = School.objects.all()
    myfilter = ProductFilter(request.GET, queryset=products)
    products = myfilter.qs
    myfilter2 = SchoolFilter(request.GET, queryset=schools)
    schools = myfilter2.qs

    # order_by_price = request.GET.get("orderby", "price")
    # if order_by_price != "":
    #     products = Product.objects.all().order_by('price')
    # sort_by_price = Product.objects.all().order_by('-price')
    # sort_by_ptitle = Product.objects.all().order_by('title')
    context = {'products': products, 'myfilter': myfilter, 'schools': schools,
    'myfilter2': myfilter2}
    template = 'products/all.html'
    return render(request, template, context)




# def all(request, school_slug):
#     school = None
#     products = Product.objects.all()
#     schools = School.objects.all()
#     if school_slug:
#         school = get_object_or_404(School, slug=school_slug)
#         products = Product.objects.filter(school=school.product)
#     context = {'products': products, 'schools': schools, 'school':school}
#     template = 'products/all.html'
#     return render(request, )



# def all(request, school_slug=None):
#     school = None
#     schools = School.objects.all()
#     products = Product.objects.filter(available=True)
#     if school_slug:
#         school = get_object_or_404(Category, slug=school_slug)
#         productsf = products.filter(school=school)
#         context = {'school': school, 'schools': schools, 'productsf': productsf}
#     else:
#         context = {'school': school, 'schools': schools, 'products': products}
#     template = 'products/all.html'
#     return render(request, template, context)
#
#     return render(request, 'store/product/product_list.html', context)

def home(request):
    products = Product.objects.all()
    categories = Category.get_all_categories()
    context = {'products': products, 'categories': categories}
    category_id = request.GET.get('category')
    if category_id:
        products = Product.get_all_products_by_categoryid(category_id=category_id)
        template = 'products/product-by-category.html'
    else:
        products = Product.objects.all()
        template = 'products/home.html'
    context = {'products': products, 'categories': categories}
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


def view_all_shirt(request):
    schools = School.objects.all()
    products = Product.objects.all().filter(title = 'p7')
    context = {"products": products, 'schools': schools}
    template = 'products/view-all-shirt.html'
    return render(request, template, context)


def view_all_skirt(request):
    schools = School.objects.all()
    products = Product.objects.all().filter(title = 'p7')
    context = {"products": products, 'schools': schools}
    template = 'products/view-all-shirt.html'
    return render(request, template, context)


def view_all_trousers(request):
    schools = School.objects.all()
    products = Product.objects.all().filter(title = 'p7')
    context = {"products": products, 'schools': schools}
    template = 'products/view-all-shirt.html'
    return render(request, template, context)

def view_all_socks(request):
    schools = School.objects.all()
    products = Product.objects.all().filter(title = 'p7')
    context = {"products": products, 'schools': schools}
    template = 'products/view-all-shirt.html'
    return render(request, template, context)

def view_all_belt(request):
    schools = School.objects.all()
    products = Product.objects.all().filter(title = 'p7')
    context = {"products": products, 'schools': schools}
    template = 'products/view-all-shirt.html'
    return render(request, template, context)
