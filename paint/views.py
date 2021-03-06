from django.shortcuts import render, get_object_or_404

from .models import Info, Publication, Technique


def home(request):
    info = get_object_or_404(Info)
    context = {
        'page': 'home',
        'image_id': info.image_id if info.image_id else None
    }
    return render(request, 'home.html', context)


def cv(request):
    info = get_object_or_404(Info)
    context = {
        'content': info.cv,
        'title': 'CV',
        'page': 'cv',
    }
    return render(request, 'info.html', context)


def statement(request):
    info = get_object_or_404(Info)
    context = {
        'content': info.statement,
        'title': 'Artist Statemnet',
        'page': 'statement',
    }
    return render(request, 'info.html', context)


def contact(request):
    info = get_object_or_404(Info)
    context = {
        'content': info.contact_text,
        'title': 'Contact',
        'page': 'contact',
    }
    return render(request, 'info.html', context)


def publications(request):
    return render(request, 'publications.html', {
        'publications': Publication.objects.all(),
        'page': 'publications',
    })


def techniques(request):
    return render(request, 'techniques.html', {
        'techniques': Technique.objects.all(),
        'page': 'techniques',
    })


def technique_detail(request, pk):
    technique = get_object_or_404(Technique, pk=pk)
    return render(request, 'technique_detail.html', {
        'technique': technique,
        'page': 'techniques',
    })
