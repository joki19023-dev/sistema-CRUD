from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('inicio/', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('post/nuevo/', views.crear_post, name='crear_post'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
]
