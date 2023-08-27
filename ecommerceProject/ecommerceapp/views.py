from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.

app_name = 'ecommerceapp'


def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(
            available=True, category=c_page)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 3)

    try:
        page = int(request.GET.get('page', '1'))

    except:
        page = 1

    try:
        products = paginator.page(page)

    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'products': products})


def prodetails(request, c_slug, product_slug):
    try:
        products = Product.objects.get(
            category__slug=c_slug, slug=product_slug)

    except Exception as e:
        raise e

    return render(request, 'products.html', {'product': products})
