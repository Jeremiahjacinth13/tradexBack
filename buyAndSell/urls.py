from django.urls import path
from . import views

app_name = 'mainApp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('posts/new', views.new_post, name = 'create_new_post'),
    path('product/new', views.new_product, name = 'create_new_product'),
    path('users/<int:user_id>', views.get_user, name = 'get_user'),
    path('posts/all', views.get_all_posts, name = 'get_all_posts'),
    path('store/<int:owner_id>', views.get_store),
    path('posts/<int:post_id>', views.get_post, name = 'get_post'),
    path('product/<int:product_id>/remove', views.remove_product, name = 'remove_product'),
    path('post/<int:post_id>/<str:operation>', views.post_operation, name = 'post_operation'),
    path('user/<int:user_id>/<str:operation>', views.edit_user_profile, name = 'edit_user_profile'),
    path('store/', views.get_store, name = 'get_store'),
    path('cart/add', views.add_to_cart, name = 'add_to_cart')
]
