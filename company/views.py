from django.shortcuts import render, get_object_or_404
from company.models import Article, Gallery


# Create your views here.
def home_page(request):
    latest_articles = Article.objects.order_by('-created_at')[:6]
    galleries = Gallery.objects.all()
    return render(request, 'company/home.html', {'articles': latest_articles, 'galleries': galleries})


def detail_page(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'company/detail.html', {'article': article})