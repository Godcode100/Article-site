from django.shortcuts import render
from django.utils import timezone
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.filter(pub_date__lte=timezone.now()).order_by("-created_on")
    return render(request, 'blog/article_list.html', {'articles':articles})