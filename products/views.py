from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .forms import ProductForm
from .models import Product


def homepage(request):
    products = Product.objects.order_by('-votes_total', 'title')
    return render(request, 'products/home.html', {'products': products})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return render(request, 'products/create.html', {
                'form': form,
                'submit_success': 'Thanks! Your Data handled Successfully'
                }
            )
        else:
            return render(request, 'products/create.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'products/create.html', {'form': form})


@login_required()
def edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            product = get_object_or_404(Product, pk=product_id)
            form = ProductForm(instance=product)
            return render(request, 'products/edit.html', {
                'form': form,
                'submit_success': 'Thanks! Your Data handled Successfully',
                'product': product
                }
            )
        else:
            return render(request, 'products/edit.html', {'form': form, 'product': product})
    else:
        form = ProductForm(instance=product)
        return render(request, 'products/edit.html', {'form': form, 'product': product})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


@login_required()
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total = F('votes_total') + 1
        product.save()
        return redirect(request.POST.get('redirect_after'))
    elif request.method == 'GET':
        return redirect('product_detail', product_id=product_id)
