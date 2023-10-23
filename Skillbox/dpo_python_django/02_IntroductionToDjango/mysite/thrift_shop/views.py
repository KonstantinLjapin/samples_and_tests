from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def skyrim(request):
    return render(request, "skyrim.html")


def fallout(request):
    return render(request, "fallout.html")


def doom(request):
    return render(request, "doom.html")


def quake(request):
    return render(request, "quake.html")


def prey(request):
    return render(request, "prey.html")
