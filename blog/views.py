from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def index(request):
    posts = Post.objects.filter(published=True)[:5]
    return render(
        request=request,
        template_name='blog/index.html',
        context={'posts': posts},
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request=request,
        template_name='blog/post-detail.html',
        context={'post': post},
    )

def post_drafts(request):
    posts = Post.objects.filter(published=False)
    return render(
        request=request,
        template_name='blog/post-drafts.html',
        context={'posts': posts},
    )


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='blog/post-new.html',
        context={'form': form},
    )


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(
        request=request,
        template_name='blog/post-edit.html',
        context={'form': form},
    )


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog:index')
    else:
        return render(
            request=request,
            template_name='blog/post-delete.html',
            context={'post': post},
        )
