from django.shortcuts import render
from django.urls import reverse



# Create your views here.

def index(request):
    return render(request, "welcome/welcome.html",{
         "name" :"index"

    })

def about(request):
    return render(request, "welcome/about.html",{
         "name" :"about"
    })

def skills(request):
    return render(request,"welcome/skills.html",{
         "name" :"skills"
    })

def projects(request):
    return render(request, "welcome/projects.html", {
        "name" : "projects"
    })