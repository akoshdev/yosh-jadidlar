from django.shortcuts import render
from django.views.generic.base import TemplateView
from aplication.models import Forums, News, Publisher
# Create your views here.
# class IndexView(TemplateView):
#     template_name = 'aplication/index.html'
#     title = 'Yosh'

class GenericView(TemplateView):
    template_name = 'aplication/forum-detail.html'
    title = 'Yosh'

class AboutView(TemplateView):
    template_name = 'aplication/about.html'
    title = 'Yosh'

# class ScientificView(TemplateView):
#     template_name = 'aplication/ilmiy-jurnal.html'
#     title = 'Yosh'


def public(request):
    publics = Publisher.objects.all()
    context = {
        'publics': publics,
    }
    return render(request, 'aplication/ilmiy-jurnallar.html', context)

def public_detail(request, id):
    public = Publisher.objects.get(id=id)
    context = {
        'public': public,
    }
    return render(request, 'aplication/ilmiy-jurnal.html', context)


def forums(request, category_id=None):
    forums = Forums.objects.filter(category_id=category_id) if category_id else Forums.objects.all()
    news = News.objects.all()
    context = {
        'forums': forums,
        'news': news,
    }
    return render(request, 'aplication/index.html', context)


def forum_detail(request, id):
    # category = ProductCategory.objects.get(id=id)
    forum = Forums.objects.get(id=id)
    # product = get_object_or_404(Product, pid=pid)

    context = {
        "forum":forum,
    }

    return render(request, 'aplication/forum-detail.html', context)

def news_detail(request, id):
    # category = ProductCategory.objects.get(id=id)
    new = News.objects.get(id=id)
    # product = get_object_or_404(Product, pid=pid)

    context = {
        "new":new,
    }

    return render(request, 'aplication/news-detail.html', context)