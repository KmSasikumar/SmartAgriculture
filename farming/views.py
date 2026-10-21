from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import math
from .models import calculate_yeild, crop_productions


# functions
def username_or_email_taken(username, mail):
    """True when the username or the email is already registered."""
    return (
        User.objects.filter(username=username).exists()
        or User.objects.filter(email__iexact=mail).exists()
    )


# Create your views here.
@login_required(login_url="sign")
def crop_yield_calculation(request):
    context = {"ans": ""}
    if request.method == "POST":
        weigth = request.POST.get("weight", "")
        area = request.POST.get("area", "")
        try:
            weigth_val = float(weigth)
            area_val = float(area)
            if area_val <= 0:
                raise ValueError("Land area must be greater than zero.")
            if weigth_val < 0:
                raise ValueError("Crop weight cannot be negative.")
        except (TypeError, ValueError) as exc:
            context["ans"] = f"Please enter valid numbers. ({exc})"
            return render(request, "cropyeild.html", context)
        result = round(weigth_val / area_val, 2)
        context["ans"] = f"{result} kg/acre"
        calculate_yeild.objects.create(
            username=request.user, weigth=weigth_val, area=area_val, result=result
        )
    return render(request, "cropyeild.html", context)


@login_required(login_url="sign")
def production_calculation(request):
    context = {"name": "", "production": "", "Revenue": "", "cost": "", "profit": "", "error": ""}
    if request.method == "POST":
        crop_name = (request.POST.get("crop_name") or "").strip()
        try:
            land_acer = float(request.POST.get("land_acer", ""))
            crop_yeild = float(request.POST.get("crop-yield", ""))
            user_cost = float(request.POST.get("user_cost", ""))
            market_price = float(request.POST.get("market_price", ""))
            if land_acer <= 0 or crop_yeild < 0 or user_cost < 0 or market_price < 0:
                raise ValueError("Land area must be greater than zero and other values cannot be negative.")
            if not crop_name:
                raise ValueError("Crop name is required.")
        except (TypeError, ValueError) as exc:
            context["error"] = f"Please enter valid values. ({exc})"
            return render(request, "production.html", context)
        totalProduction = round(land_acer * crop_yeild, 2)
        totalRevenue = round(totalProduction * market_price, 2)
        totalCost = round(land_acer * user_cost, 2)
        profit = round(totalRevenue - totalCost, 2)
        context["name"] = crop_name
        context["production"] = totalProduction
        context["Revenue"] = totalRevenue
        context["cost"] = totalCost
        context["profit"] = profit
        crop_productions.objects.create(
            username=request.user,
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
    return render(request, "production.html", context)


@login_required(login_url="sign")
def loan_calculate(request):
    return render(request, "finacnce.html")


def crop_health(request):
    return render(request, "crophealth.html")


def register(request):
    context = {"error": ""}
    if request.method == "POST" and "signin" in request.POST:
        fname = (request.POST.get("fname") or "").strip()
        lname = (request.POST.get("lname") or "").strip()
        username = (request.POST.get("username") or "").strip()
        mail = (request.POST.get("mail") or "").strip()
        password = request.POST.get("password") or ""
        confirmpassword = request.POST.get("confirmpassword") or ""

        if not all([fname, lname, username, mail, password, confirmpassword]):
            context["error"] = "All fields are required."
        elif password != confirmpassword:
            context["error"] = "Passwords do not match."
        elif username_or_email_taken(username, mail):
            context["error"] = "That username or email is already registered."
        else:
            user = User.objects.create_user(
                username=username,
                email=mail,
                password=password,
                first_name=fname.capitalize(),
                last_name=lname.capitalize(),
            )
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect("/")

    return render(request, "register.html", context)


def sign(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("password")
        check = auth.authenticate(username=username, password=password)
        if check is None:
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
