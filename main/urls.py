from django.urls import path
from main import views


urlpatterns = [
    path('', views.index,name='index'),
    path('article/<int:pk>', views.article, name='get_article'),
    path('author/<int:pk>', views.author, name='author'),
    path('create', views.create, name='create'),
    path('article',views.article1,name='article')
]