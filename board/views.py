from django.shortcuts import render

def index(request):
    return render(request, 'board/index.html')

def news(request):
    return render(request, 'board/news.html')

def bullet(request):
    return render(request, 'board/bullet.html')

def resp(request):
    return render(request, 'board/resp.html')