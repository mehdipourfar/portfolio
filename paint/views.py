from django.shortcuts import render, get_object_or_404

from .models import Info, Publication, Technique


def home(request):
    return render(request, 'base.html')


def cv(request):
    info = get_object_or_404(Info)
    context = {
        'content': info.cv,
        'title': 'CV'
    }
    return render(request, 'info.html', context)


def statement(request):
    info = get_object_or_404(Info)
    context = {
        'content': info.statement,
        'title': 'Artist Statemnet'
    }
    return render(request, 'info.html', context)


def contact(request):
    info = get_object_or_404(Info)
    context = {
        'content': info.contact_text,
        'title': 'Contact'
    }
    return render(request, 'info.html', context)


def publications(request):
    return render(request, 'publications.html', {
        'publications': Publication.objects.all()
    })


def techniques(request):
    return render(request, 'techniques.html', {
        'techniques': Technique.objects.all()
    })
