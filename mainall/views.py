from django.shortcuts import render
from .models import Reviews
from .forms import ReviewsForm
from django.http.response import JsonResponse
import json


def index(request):
    return render(request, 'mainall/index.html')


def feedback(request):
    error = ''
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'ошибка'

    form = ReviewsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainall/feedback.html', context)


def post_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = ReviewsForm(data)
        if form.is_valid():
            form.save()
        return JsonResponse({'msg': 'ok'})
    else:
        return JsonResponse({'msg': 'ne ok'})


def login(request):
    return render(request, 'mainall/login.html')


def add_user(request):
    return render(request, 'mainall/add_user.html')


def add_devices(request):
    return render(request, 'mainall/add_devices.html')


def map_PGU(request):
    return render(request, 'mainall/map_PGU.html')