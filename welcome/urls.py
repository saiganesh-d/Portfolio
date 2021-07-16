from django.urls import path

from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("about",views.about, name="about"),
    path("skils",views.skills,name="skills"),
    path("projects",views.projects,name="projects"),
    path("cars",views.cars,name="cars"),
]
