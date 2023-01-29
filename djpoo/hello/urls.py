from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("rami", views.rami, name="rami"),
    path("david", views.david, name="david"),
    path("nizar", views.nizar, name="nizar")

]
