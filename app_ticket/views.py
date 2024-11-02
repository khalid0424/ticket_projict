from django.shortcuts import render , HttpResponse, get_object_or_404

from models import Show, Teatr ,Ticketorder ,Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'theater/home.html', {'movies': movies})

def teatr(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    showtimes = movie.showtimes.all()  
    return render(request, 'theater/movie_detail.html', {'movie': movie, 'showtimes': showtimes})


