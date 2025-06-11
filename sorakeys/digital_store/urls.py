from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_view, name='home_view'),
    path('catalog/', catalog_view, name='catalog_view'),
    path('cart/', cart_view, name='cart_view'),
    path('login/', login_view, name='login_view'),
    path('about/', about_view, name='about_view'),
    path('contacts/', contacts_view, name='contacts_view'),
    path('find_us/', find_us_view, name='find_us_view'),

    path('admin_panel/', admin_panel_view, name='admin_panel_view'),
    # Товары
    path('products/', ProductListView.as_view(), name='product_list_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('products/create/', ProductCreateView.as_view(), name='product_create_view'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_view'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    # Категории
    path('categories/', CategoryListView.as_view(), name='category_list_view'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail_view'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create_view'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update_view'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete_view'),
    # Корзина
    path('carts/', CartListView.as_view(), name='cart_list_view'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart_detail_view'),
    path('carts/create/', CartCreateView.as_view(), name='cart_create_view'),
    path('carts/<int:pk>/update/', CartUpdateView.as_view(), name='cart_update_view'),
    path('carts/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete_view'),
    # Заказы
    path('orders/', OrderListView.as_view(), name='order_list_view'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail_view'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create_view'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update_view'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete_view'),
    # Издатели
    path('publishers/', PublisherListView.as_view(), name='publisher_list_view'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail_view'),
    path('publishers/create/', PublisherCreateView.as_view(), name='publisher_create_view'),
    path('publishers/<int:pk>/update/', PublisherUpdateView.as_view(), name='publisher_update_view'),
    path('publishers/<int:pk>/delete/', PublisherDeleteView.as_view(), name='publisher_delete_view'),
    # Платформы
    path('platforms/', PlatformListView.as_view(), name='platform_list_view'),
    path('platforms/<int:pk>/', PlatformDetailView.as_view(), name='platform_detail_view'),
    path('platforms/create/', PlatformCreateView.as_view(), name='platform_create_view'),
    path('platforms/<int:pk>/update/', PlatformUpdateView.as_view(), name='platform_update_view'),
    path('platforms/<int:pk>/delete/', PlatformDeleteView.as_view(), name='platform_delete_view'),
    # Скидки
    path('discounts/', DiscountListView.as_view(), name='discount_list_view'),
    path('discounts/<int:pk>/', DiscountDetailView.as_view(), name='discount_detail_view'),
    path('discounts/create/', DiscountCreateView.as_view(), name='discount_create_view'),
    path('discounts/<int:pk>/update/', DiscountUpdateView.as_view(), name='discount_update_view'),
    path('discounts/<int:pk>/delete/', DiscountDeleteView.as_view(), name='discount_delete_view'),
]