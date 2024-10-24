from django.shortcuts import render

# Create your views here.


def home(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'third_task/platform.html', context)


def magazine(request):
    title = 'Игры'
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunc 2077'
    game3 = 'PayDay 2'
    button_pay = 'Купить'
    button_back = 'Вернуться обратно'
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'button_pay': button_pay,
        'button_back': button_back
    }
    return render(request, 'third_task/games.html', context)


def basket(request):
    title = 'Корзина'
    text = 'Вернитесь в магазин и купите что-нибудь'
    text2 = 'Ну пожалуйста)'
    button_back = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'text2': text2,
        'button_back': button_back
    }
    return render(request, 'third_task/cart.html', context)
