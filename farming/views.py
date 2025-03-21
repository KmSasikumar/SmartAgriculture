from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import math
from .models import calculate_yeild, crop_productions


# functions
def checkemail(mail, UserName):
    try:
        user_name = User.objects.get(username=UserName)
        return False
    except:
        return True


# Create your views here.
@login_required(login_url="sign")
def crop_yield_calculation(request):
    user = User.objects.get(username=request.user)
    # user = get_object_or_404(User, username=request.user)
    print(user)
    context = {"ans": ""}
    if request.method == "POST":
        weigth = request.POST.get("weight")
        area = request.POST.get("area")
        print(weigth, area)
        result = float(weigth) / float(area)
        result = round(result, 2)
        ans = f"{result} kg/acre"
        context["ans"] = ans
        final = calculate_yeild.objects.create(
            username=user, weigth=weigth, area=area, result=result
        )
        final.save()
    return render(request, "cropyeild.html", context)


@login_required(login_url="sign")
def production_calculation(request):
    context = {"name": "", "production": "", "Revenue": "", "cost": "", "profit": ""}
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        crop_name = request.POST.get("crop_name")
        land_acer = request.POST.get("land_acer")
        crop_yeild = request.POST.get("crop-yield")
        user_cost = request.POST.get("user_cost")
        market_price = request.POST.get("market_price")
        # print(crop_name, crop_yeild, user_cost, market_price)
        totalProduction = round(float(land_acer) * float(crop_yeild), 2)
        totalRevenue = round(float(totalProduction) * float(market_price), 2)
        totalCost = round(float(land_acer) * float(user_cost), 2)
        profit = round(float(totalRevenue) - float(totalCost), 2)
        context["name"] = crop_name
        context["production"] = totalProduction
        context["Revenue"] = totalRevenue
        context["cost"] = totalCost
        context["profit"] = profit
        final = crop_productions.objects.create(
            username=user,
            crop_name=crop_name,
            land_acer=land_acer,
            crop_yeild=crop_yeild,
            user_cost=user_cost,
            market_price=market_price,
            totalProduction=totalProduction,
            totalRevenue=totalRevenue,
            totalCost=totalCost,
            profit=profit,
        )
        final.save()
    return render(request, "production.html", context)


@login_required(login_url="sign")
def loan_calculate(request):
    return render(request, "finacnce.html")


def crop_health(request):
    return render(request, "crophealth.html")


def register(request):
    if "signin" in request.POST:
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        mail = request.POST.get("mail")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if password != confirmpassword:
            print("Password not matched")

        elif checkemail(mail, username):
            user = User.objects.create_user(
                username=username,
                email=mail,
                password=password,
                first_name=fname.capitalize(),
                last_name=lname.capitalize(),
            )
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect("/")

    return render(request, "register.html")


def sign(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("password")
        print(username, password)
        check = auth.authenticate(username=username, password=password)
        print(check)
        if check == None:
            print("redirect to login")
            return redirect("/register")
        else:
            auth.login(request, check)
            return redirect("/")

    return render(request, "signin.html")


def home(request):
    return render(request, "index.html")


def article1(request):
    return render(request, "article 1.html")


def article2(request):
    return render(request, "article 2.html")


def article3(request):
    return render(request, "article 3.html")


def soilClassification(request):
    return render(request, "soil-classification.html")


def soilType(request):
    return render(request, "soil type.html")


@login_required(login_url="/sign")
def signout(request):
    auth.logout(request)
    return redirect("/sign")
