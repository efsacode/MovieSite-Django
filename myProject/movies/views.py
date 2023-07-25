from django.shortcuts import render

categories = [
    "Animation",
    "Sci-Fi",
    "Romantic"
]

filmler = [
{   
    "id":1,
    "title": "movie_1",
    "category": "Animation",
    "image": "1.jpg",
    "anasayfa": True,
},

{
    "id":2, #id ekledik ve her bir film icin ayri ayri id tanimladik
    "title": "movie_2",
    "category": "Sci-Fi",
    "image": "2.jpg",
    "anasayfa": True,
},

{
    "id":3,
    "title": "movie_3",
    "category": "Romantic",
    "image": "3.jpg",
    "anasayfa": False,
},

]

def home(request):
    data = {
        "category": categories, #categories listesini data sozlugune ekledik ve key tanimladik
        "movie": filmler
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "category": categories, #categories listesini data sozlugune ekledik ve key tanimladik
        "movie": filmler
    }
    return render(request, "movies.html",data)

def movie_details(request):
    data = {
        "id": id,
    }
    return render(request, "details.html",data)
   

# Create your views here.
