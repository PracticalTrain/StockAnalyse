from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from .models import News

PAGE_SIZE = 15
AFTER_RANGE_NUM = 5
BEFORE_RANGE_NUM = 4


def index(request):

    return get_news_by_pages(request, 1)


def get_news_by_pages(request, page_num):
    page = int(page_num)
    news_list = News.objects.all().order_by('-pub_time')
    paginator = Paginator(news_list, PAGE_SIZE)
    try:
        return_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        return_list = paginator.page(1)
    if page+AFTER_RANGE_NUM >= paginator.num_pages:
        page_range = [i for i in range(page, paginator.num_pages)]
    else:
        page_range = [i for i in range(page, page+AFTER_RANGE_NUM)]
    return render(request, 'news/index.html', {'news_list': return_list,
                                               'page_range': page_range,
                                               'curr_page': page,
                                               'num_pages': paginator.num_pages})


def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html', {'news': news})