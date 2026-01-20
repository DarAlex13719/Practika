from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Nomera

MENU = {'главная': '/', 'пост': '/post', 'о блоге': '/about', 'комментарии': '/com'}

def com (request):
    nomera = Nomera.objects.all()
    title = 'Добавить комментарии'
    data = {'menu': MENU, 'title': title, 'nomera': nomera}
    return render(request, "./com.html", context=data)

def thanks (request):
    user_name = request.POST['user_name']
    email = request.POST['email']
    comment = request.POST['comment']
    Nomera.objects.create(user_name=user_name, email=email, comment=comment)
    title = 'Спасибо'
    data = {'menu': MENU, 'title': title, 'user_name': user_name}
    return render(request, "./thanks.html", context=data)
