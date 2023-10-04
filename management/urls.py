from django.urls import path
from .import views

urlpatterns = [
    path('show', views.Booklistview, name='books'),
    path('barcode', views.BooklistviewTest, name='booksTest'),
    path('search-blogs', views.BooklistviewTest, name='search_blogs'),
    # path('addData', views.addData),
]
