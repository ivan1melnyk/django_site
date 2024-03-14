from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('quote/', views.quote, name='quote'),
    path('tag/', views.tag, name='tag'),
    path('<int:pk>', views.AuthorView.as_view(), name='author'),
    path('add_author/', views.add_author, name='add_author'),
]
