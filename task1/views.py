from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from .forms import RegistrationForm
from .models import Game, Buyer, News


# Create your views here.
def registration_page(request):
    users = ["user", "qwerty", "qwer"]
    info = dict()

    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        print(name, password, repeat_password, age)

        if password != repeat_password:
            info["error"] = "Пароли не совпадают!"
        if int(age) < 18:
            info["error"] = "Вы должны быть старше 18 лет!"
        if name in users:
            info["error"] = "Пользователь уже существует!"
        if password == repeat_password and int(age) > 17 and name not in users:
            info["info"] = f"Приветствуем, {name}!"

    return render(request, "registration_page.html", info)


def registration_page_django(request):
    info = dict()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if password == repeat_password and int(age) > 17 and not Buyer.objects.all().filter(name=name):
                info["info"] = f"Приветствуем, {name}!"
                Buyer.objects.create(name=name, balance=0.0, age=age)
            elif password != repeat_password:
                info["error"] = "Пароли не совпадают!"
            elif int(age) < 18:
                info["error"] = "Вы должны быть старше 18 лет!"
            elif Buyer.objects.all().filter(name=name):
                info["error"] = "Пользователь уже существует!"
    else:
        form = RegistrationForm()
    info["form"] = form
    return render(request, "registration_page_django.html", info)


def test(request):
    name = request.GET.get("name", "user")
    age = request.GET.get("age", "18")
    return HttpResponse(f"Hello, {name} {age}!")


def platform_page(request):
    return render(request, "platform.html")


def games_page(request):
    list_games = Game.objects.all()
    context = {
        "list_games": list_games,
    }
    return render(request, "games.html", context)


def cart_page(request):
    return render(request, "cart.html")


def paginator_news(request):
    news = News.objects.all().order_by("-date")
    paginator = Paginator(news, 3)
    page_number = request.GET.get("page")
    news_obj = paginator.get_page(page_number)
    return render(request, "news.html", {"news": news_obj})
