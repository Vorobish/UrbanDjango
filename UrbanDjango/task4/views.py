# task4

from django.shortcuts import render

# Create your views here.


def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/platform.html', context)


def games(request):
    title = 'Игры'
    button_pay = 'Купить'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'title': title,
        'games': games,
        'button_pay': button_pay,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    title = 'Корзина'
    text = 'Вернитесь в магазин и купите что-нибудь'
    text2 = 'Ну пожалуйста)'
    context = {
        'title': title,
        'text': text,
        'text2': text2,
    }
    return render(request, 'fourth_task/cart.html', context)


def menu(request):
    return render(request, 'fourth_task/menu.html')