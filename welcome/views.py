from django.shortcuts import render
from django.urls import reverse
import joblib
import numpy as np
from django.shortcuts import HttpResponse, HttpResponseRedirect,render



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


def cars(request):
    rf=joblib.load('final.sav')
    if request.method == "GET":
        return render(request,"welcome/cars.html")

    
       
    Year =request.POST['Year']
    Present_Price =request.POST['Present_Price']
    Kms_Driven =request.POST['Kms_Driven']
    Owner =request.POST['Owner']
    Fuel_Type_Petrol =request.POST['Fuel_Type_Petrol']
    Seller_Type_Individual =request.POST['Seller_Type_Individual']
    Transmission_Mannual =request.POST['Transmission_Mannual']
    Year= int(Year)
    Year= 2021-Year
    Present_Price=float(Present_Price)
    
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0



    prediction=rf.predict([[Year,Present_Price,Kms_Driven,Owner,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    if output<0:
        return render(request,"welcome/cars.html",{"prediction_texts":"Sorry you cannot sell this car"})
    else:
            return render(request,"welcome/cars.html",{"prediction_text":"You Can Sell The Car at {}".format(output)})
    
       

    