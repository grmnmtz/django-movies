from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Jaws',
            'year': 1996,
        },
        {
             'id': 4,
            'title': 'Sharknado',
            'year': 2001
        },
        {
             'id': 3,
            'title': 'The Sharks',
            'year': 1999
        }
    ]
}

template_name = 'movies/movies.html'

def movies(request):
    return render(request, template_name, data)

def home(request):
    return HttpResponse("Home page")