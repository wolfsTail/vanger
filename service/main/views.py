from django.shortcuts import render

from slider.models import Slider


def get_index(request):
    context = {}
    slides = Slider.objects.select_related('owner', 'image').all()
    context = {'slides': slides}
    return render(request, "main/index.html", context)
