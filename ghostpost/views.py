from django.shortcuts import render
from ghostpost.models import GhostPoster
from ghostpost.forms import RoastorBoastAddForm


def index(request):
    html = "index.html"

    post = GhostPoster.objects.all()

    return render(request, html, {'data': post})


def ghostpostaddview(request):
    html = "post_add_form.html"

    form = RoastorBoastAddForm()

    return render(request, html, {'form': form})
