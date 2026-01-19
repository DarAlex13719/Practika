from django.http import HttpResponse


def main_page(request):
    return HttpResponse("<h1>Главная страница</h1>")


def about_blog (request):
    return HttpResponse("<h1>О блоге</h1>")


def post (request):
    return HttpResponse("<h1>Страница поста</h1>")