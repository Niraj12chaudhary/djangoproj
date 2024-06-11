# from django.urls import path
# from .views import home, add_numbers

# urlpatterns = [
#     path('add/', add_numbers, name='add-numbers'),
#       path('', home, name='home'),

# ]


from django.urls import path
from .views import home, add_numbers, subtract_numbers, multiply_numbers, divide_numbers

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_numbers, name='add-numbers'),
    path('subtract/', subtract_numbers, name='subtract-numbers'),
    path('multiply/', multiply_numbers, name='multiply-numbers'),
    path('divide/', divide_numbers, name='divide-numbers'),
]
