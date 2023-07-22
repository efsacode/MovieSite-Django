from django.shortcuts import render

categories = [
    "Action",
    "Fantasy",
    "Horror"
]

filmler = [
{
    "title": "movie_1",
    "category": "Action",
    "image": "https://images-na.ssl-images-amazon.com/images/S/pv-target-images/bef717a48915cb3a77fe1f496b76f16b4348905237c55bb72c7ae374dbc793b8._RI_TTW_.jpg",
},

    "movie_1",
    "movie_2",
    "movie_3"
]

def home(request):
    data = {
        "category": categories, #categories listesini data sozlugune ekledik ve key tanimladik
        "movie": filmler
    }
    return render(request, "index.html", data)

def movies(request):
    return render(request, "movies.html")

# Create your views here.
