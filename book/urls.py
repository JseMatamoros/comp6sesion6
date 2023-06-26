from django.urls import path
# from .views import IndexPageView, list_books
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('listbook/', views.list_books, name='list_books'),
]


