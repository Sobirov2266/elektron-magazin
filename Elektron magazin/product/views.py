from django.core.paginator import Paginator
from django.shortcuts import render
from product.models import Product, Category

SORTING = {
    'Arzon': 'price',
    'Qimmat': '-price',
    'Yangi': '-id',
    'Eski': 'id',

}


def home(request):
    products = Product.objects.all()
    print(products)
    return render(
        request=request,
        template_name='index.html',
        context={
            'products': products
        }

    )


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(
        request=request,
        template_name='product/product_detail.html',
        context={
            'product': product
        }
    )


def products(request):
    cat = request.GET.get('cat', 0)
    page: str = request.GET.get('page', 1)
    per_page: str = request.GET.get('per-page', 6)
    sorting: str = request.GET.get('sorting', 'Yangi')
    min_price: str = request.GET.get('min_price', 0)
    max_price: str = request.GET.get('max_price', 1000000000000)
    if cat:
        product_list = Product.objects.filter(category_id=cat)
    else:
        product_list = Product.objects.all()
    product_list = product_list.filter(price__lte=max_price, price__gte=min_price).order_by(SORTING[sorting])
    category_list = Category.objects.all()
    paginator = Paginator(
        object_list=product_list,
        per_page=per_page

    )
    page = int(page)

    page = page if page <= paginator.num_pages else paginator.num_pages
    product_list_page = paginator.get_page(page)

    return render(
        request=request,
        template_name='product/products.html',
        context={
            'products': product_list_page,
            'categories': category_list,
            'paginator': paginator,
            'current_page': int(page),
            'current_category': int(cat),
            'per-page': per_page,
            'sorting': sorting,
        }
    )


def search(request):
    search_text = request.GET.get('search', None)
    product_list = Product.objects.filter(name__icontains=search_text)
    category_list = Category.objects.all()
    return render(
        request=request,
        template_name='product/products.html',
        context={
            'products': product_list,
            'categories': category_list
        }
    )
