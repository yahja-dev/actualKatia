from django.shortcuts import render


def about_view(request):
    return render(request, "core/home.html")