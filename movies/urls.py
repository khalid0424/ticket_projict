from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('theaters/', views.teatr_list, name='teatr_list'),  # Ислоҳ шуд
    path('shows/', views.show_list, name='show_list'),
    path('orders/', views.ticket_order_list, name='ticket_order_list'),
]
