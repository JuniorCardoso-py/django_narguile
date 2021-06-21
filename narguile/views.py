from narguile.models import Narguile
from django.shortcuts import render

# Create your views here.
def list_all(request):
    narguile = Narguile.objects.all()
    return render(request, 'narguile.html', {'narguile':narguile})
