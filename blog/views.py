from django.shortcuts import render

# Create your views here.
def article_list(request):
    return render(request, 'blog/article_list.html', {})