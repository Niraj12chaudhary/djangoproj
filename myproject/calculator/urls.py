# email_app/urls.py

from django.urls import path
from .views import home, add_numbers_get, subtract_numbers_get, multiply_numbers_get, divide_numbers_get
from .views import add_numbers_post, subtract_numbers_post, multiply_numbers_post, divide_numbers_post

urlpatterns = [
    path('', home, name='home'),
    # GET requests
    path('add/', add_numbers_get, name='add-numbers-get'),
    path('subtract/', subtract_numbers_get, name='subtract-numbers-get'),
    path('multiply/', multiply_numbers_get, name='multiply-numbers-get'),
    path('divide/', divide_numbers_get, name='divide-numbers-get'),
    # POST requests
    path('add_post/', add_numbers_post, name='add-numbers-post'),
    path('subtract_post/', subtract_numbers_post, name='subtract-numbers-post'),
    path('multiply_post/', multiply_numbers_post, name='multiply-numbers-post'),
    path('divide_post/', divide_numbers_post, name='divide-numbers-post'),
]
