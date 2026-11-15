from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Post


# LISTAR (Index)
def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, 'posts/lista_posts.html', {'posts': posts})


# DETALLE (Detail)
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


# CREAR (Create)
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Crear'})


# EDITAR (Update)
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'post': post, 'accion': 'Editar'})


# BORRAR (Delete)
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})


def inicio(request):
    return lista_posts(request)


def acerca(request):
    return render(request, 'posts/acerca.html')
