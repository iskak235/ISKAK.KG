from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:cat_slug>/', views.category_view, name='category_page'),
    path('post/<int:pk>/', views.detail_view, name='detail_page'), # Жаңы сап
]