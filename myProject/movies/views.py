from django.shortcuts import render

categories = [
    "Animation",
    "Sci-Fi",
    "Romantic"
]

filmler = [
{
    "title": "movie_1",
    "category": "Animation",
    "image": "1.jpg",
    "anasayfa": True,
},

{
    "title": "movie_2",
    "category": "Sci-Fi",
    "image": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
    "anasayfa": True,
},

{
    "title": "movie_3",
    "category": "Romantic",
    "image": "https://upload.wikimedia.org/wikipedia/tr/thumb/8/8e/Bay_Evet.jpg/220px-Bay_Evet.jpg",
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

# Create your views here.
