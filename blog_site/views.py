from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login,authenticate
# Create your views here.
def home(request,*args,**kwargs):
    user=request.user
    if user.is_authenticated:
        return HttpResponse(f"your are already authenticated as {user.email}")
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("your account is created successfully")
    return render(request,'register.html')

