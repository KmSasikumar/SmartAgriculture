from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("sign/", views.sign, name="sign"),
    path("signout/", views.signout, name="signout"),
    path("register/", views.register, name="register"),
    path("cropyeild/", views.crop_yield_calculation, name="cropyeild"),
    path("production/", views.production_calculation, name="production"),
    path("finance/", views.loan_calculate, name="finance"),
    path("cropHealth/", views.crop_health, name="crophealth"),
    path("article1/", views.article1, name="article1"),
    path("article2/", views.article2, name="article2"),
    path("article3/", views.article3, name="article3"),
    path("soilClassification/" , views.soilClassification, name="soil_classification"),
    path("soilType/" , views.soilType, name="soil_type"),
]
