from django.shortcuts import render
from albums.models import Albums
from musicians.models import Musicians

# Create your views here.
def home(request):
    musicians = Musicians.objects.all()
    albums = Albums.objects.all()
    return render(request, "home.html", {"musicians": musicians, "albums": albums})
    