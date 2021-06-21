from django.shortcuts import redirect, render

from narguile.forms import NarguileForm
from narguile.models import Narguile

# Create your views here.


def list_all(request):
    narguile = Narguile.objects.all()
    return render(request, 'narguile.html', {'narguile': narguile})


def update(request, id):
    narguile = Narguile.objects.get(id=id)
    form = NarguileForm(request.POST or None)
    if request.method == 'POST' and id:
        form = NarguileForm(request.POST, request.FILES, instance=narguile)
        if form.is_valid():
            form.save()
        return redirect('list_all')
    return render(request, 'forms.html', {'form': form})


def create(request):
    form = NarguileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_all')
    return render(request, 'forms.html', {'form': form})


def delete(request, id):
    Narguile.objects.get(id=id).delete()
    return redirect('list_all')
