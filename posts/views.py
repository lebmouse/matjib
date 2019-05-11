from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Category, SubCategory, Post


def home(request):
    categorys = Category.objects.all()
    item = []
    for category in (categorys):
        item.append({'category': category,
                     'sub_categorys': SubCategory.objects.filter(parent_id=category.id), })

    # TODO: posts 리스트 만들어 추가하기

    post = Post.objects.all()
    context = {'categorys': item, 'posts': post}

    return render(request, 'home.html', context)


def detail(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    #     post = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'detail.html', context)
