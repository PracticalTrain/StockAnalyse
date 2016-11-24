from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News


def index(request):
    news_list = News.objects.order_by('-pub_time')[:5]
    return render(request, 'news/index.html', {'news_list': news_list})


def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html', {'news': news})
