from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,"index.html")
def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        print("work")
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=UserCreationForm()
    return render(request,"registration/register.html",{'form':form})
def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")
    
    
    
    
