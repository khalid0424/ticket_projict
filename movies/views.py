from django.shortcuts import render
from .models import Movie, Teatr, Show, Ticketorder


def home(request):
    return render(request, 'home.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'templates/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'templates/movie_detail.html', {'movie': movie})

def teatr_list(request):
    theaters = Teatr.objects.all()
    return render(request, 'templates/teatr_list.html', {'theaters': theaters})

def show_list(request):
    shows = Show.objects.all()
    return render(request, 'templates/show_list.html', {'shows': shows})

def ticket_order_list(request):
    orders = Ticketorder.objects.all()
    return render(request, 'templates/ticket_order_list.html', {'orders': orders})
