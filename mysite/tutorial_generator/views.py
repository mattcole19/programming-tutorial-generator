from django.shortcuts import render
from django.http import HttpResponse
from .services import generate_tutorial

def index(request):

    if request.method == 'POST':
        language = request.POST.get('language')
        concept = request.POST.get('concept')

        prompt = generate_tutorial(concept, language)
        return render(request, 'tutorial_generator/index.html', context={'prompt': prompt})

    return render(request, 'tutorial_generator/index.html', {})