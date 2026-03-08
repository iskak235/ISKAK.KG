from django.shortcuts import render, get_object_or_404 # get_object_or_404 кошулду
from .models import MyHistory

def index(request):
    items = MyHistory.objects.all().order_by('-date_added')
    return render(request, 'main/index.html', {'items': items, 'title': 'Башкы бет'})

def category_view(request, cat_slug):
    items = MyHistory.objects.filter(category=cat_slug).order_by('-date_added')
    titles = {
        'STUDY': 'Окуу жана билим',
        'WORK': 'Ишкердик жана жумуш',
        'GAMES': 'Оюндар жана хобби',
        'VILLAGE': 'Айыл жана эс алуу'
    }
    context = {
        'items': items,
        'title': titles.get(cat_slug, 'Бөлүм')
    }
    return render(request, 'main/index.html', context)

# МЫНА УШУЛ ФУНКЦИЯНЫ КОШУҢУЗ:
def detail_view(request, pk):
    item = get_object_or_404(MyHistory, pk=pk)
    return render(request, 'main/detail.html', {'item': item})