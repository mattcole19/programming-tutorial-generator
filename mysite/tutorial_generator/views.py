from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    if request.method == 'POST':
        language = request.POST.get('language')
        concept = request.POST.get('concept')

        # TODO: Generate response here
        prompt = f'{language}, {concept}'
        return render(request, 'tutorial_generator/index.html', context={'prompt': prompt})

    return render(request, 'tutorial_generator/index.html', {})