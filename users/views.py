from django.shortcuts import render

def index(request):

    return render(request, 'inicio/index.html')

def index_en(request):

    return render(request, 'inicio/index_en.html')

def index_es(request):

    return render(request, 'inicio/index_es.html')