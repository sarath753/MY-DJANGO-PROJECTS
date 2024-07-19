from django.shortcuts import render, get_object_or_404, redirect
from .models import Movies

def listmovies(request):
    movielist = Movies.objects.all()
    return render(request,'reviews/moviedisplay.html',{'movielist' : movielist})

def detailedmovie(request,id):
    movie = get_object_or_404(Movies,id=id)
    return render(request,'reviews/moviedetaileddisplay.html',{'movie' : movie})

def addmovie(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('desc')
        director = request.POST.get('director')
        cast = request.POST.get('cast')
        zoner = request.POST.get('zoner')
        poster = request.POST.get('poster')

        movie = Movies(title=title,description=description,director=director,cast=cast,zoner=zoner,poster=poster)
        movie.save()
        return redirect("simpledisplaymovies")
    return render(request,"reviews/movieadd.html")