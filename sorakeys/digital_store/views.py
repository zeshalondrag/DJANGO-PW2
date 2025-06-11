from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

def home_view(request):
    return render(request, 'pages/home.html')

def catalog_view(request):
    return render(request, 'pages/catalog.html')

def cart_view(request):
    return render(request, 'pages/cart.html')

def login_view(request):
    return render(request, 'pages/login.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contacts_view(request):
    return render(request, 'pages/contacts.html')

def find_us_view(request):
    return render(request, 'pages/find_us.html')

def admin_panel_view(request):
    return render(request, 'admin_panel/admin_panel.html')

class ProductListView(ListView):
    model = Product
    template_name = 'admin_panel/products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'admin_panel/products/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin_panel/products/product_form.html'
    success_url = reverse_lazy('product_list_view')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin_panel/products/product_form.html'
    success_url = reverse_lazy('product_list_view')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admin_panel/products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list_view')

class CategoryListView(ListView):
    model = Category
    template_name = 'admin_panel/categories/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'admin_panel/categories/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'admin_panel/categories/category_form.html'
    success_url = reverse_lazy('category_list_view')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'admin_panel/categories/category_form.html'
    success_url = reverse_lazy('category_list_view')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'admin_panel/categories/category_confirm_delete.html'
    success_url = reverse_lazy('category_list_view')

class CartListView(ListView):
    model = Cart
    template_name = 'admin_panel/carts/cart_list.html'
    context_object_name = 'carts'

class CartDetailView(DetailView):
    model = Cart
    template_name = 'admin_panel/carts/cart_detail.html'
    context_object_name = 'cart'

class CartCreateView(CreateView):
    model = Cart
    form_class = CartForm
    template_name = 'admin_panel/carts/cart_form.html'
    success_url = reverse_lazy('cart_list_view')

class CartUpdateView(UpdateView):
    model = Cart
    form_class = CartForm
    template_name = 'admin_panel/carts/cart_form.html'
    success_url = reverse_lazy('cart_list_view')

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'admin_panel/carts/cart_confirm_delete.html'
    success_url = reverse_lazy('cart_list_view')

class OrderListView(ListView):
    model = Order
    template_name = 'admin_panel/orders/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'admin_panel/orders/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'admin_panel/orders/order_form.html'
    success_url = reverse_lazy('order_list_view')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'admin_panel/orders/order_form.html'
    success_url = reverse_lazy('order_list_view')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'admin_panel/orders/order_confirm_delete.html'
    success_url = reverse_lazy('order_list_view')

class PublisherListView(ListView):
    model = Publisher
    template_name = 'admin_panel/publishers/publisher_list.html'
    context_object_name = 'publishers'

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'admin_panel/publishers/publisher_detail.html'
    context_object_name = 'publisher'

class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'admin_panel/publishers/publisher_form.html'
    success_url = reverse_lazy('publisher_list_view')

class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'admin_panel/publishers/publisher_form.html'
    success_url = reverse_lazy('publisher_list_view')

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'admin_panel/publishers/publisher_confirm_delete.html'
    success_url = reverse_lazy('publisher_list_view')

class PlatformListView(ListView):
    model = Platform
    template_name = 'admin_panel/platforms/platform_list.html'
    context_object_name = 'platforms'

class PlatformDetailView(DetailView):
    model = Platform
    template_name = 'admin_panel/platforms/platform_detail.html'
    context_object_name = 'platform'

class PlatformCreateView(CreateView):
    model = Platform
    form_class = PlatformForm
    template_name = 'admin_panel/platforms/platform_form.html'
    success_url = reverse_lazy('platform_list_view')

class PlatformUpdateView(UpdateView):
    model = Platform
    form_class = PlatformForm
    template_name = 'admin_panel/platforms/platform_form.html'
    success_url = reverse_lazy('platform_list_view')

class PlatformDeleteView(DeleteView):
    model = Platform
    template_name = 'admin_panel/platforms/platform_confirm_delete.html'
    success_url = reverse_lazy('platform_list_view')

class DiscountListView(ListView):
    model = Discount
    template_name = 'admin_panel/discounts/discount_list.html'
    context_object_name = 'discounts'

class DiscountDetailView(DetailView):
    model = Discount
    template_name = 'admin_panel/discounts/discount_detail.html'
    context_object_name = 'discount'

class DiscountCreateView(CreateView):
    model = Discount
    form_class = DiscountForm
    template_name = 'admin_panel/discounts/discount_form.html'
    success_url = reverse_lazy('discount_list_view')

class DiscountUpdateView(UpdateView):
    model = Discount
    form_class = DiscountForm
    template_name = 'admin_panel/discounts/discount_form.html'
    success_url = reverse_lazy('discount_list_view')

class DiscountDeleteView(DeleteView):
    model = Discount
    template_name = 'admin_panel/discounts/discount_confirm_delete.html'
    success_url = reverse_lazy('discount_list_view')