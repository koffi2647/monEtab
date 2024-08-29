
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from .models import User
from .forms import  UserForm


# Create your views here.
def index(request):
    users = User.objects.all()
    
    context = { 'users': users }
    return render(request,'user/index.html',context)

def ajouterUser(request):
    
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('user:index')
        else:
            return render(request, 'user:modifierUser', context)        
    form = UserForm()
    context = {'form': form}
    return render(request, 'user/ajouterUser.html', context) 
     
     
def modifierUser(request,id):
    user = User.objects.get(id=id)
    context = {'title':'modification utilisateur'}
    
    if request.method == 'POST':
        form = UserForm(request.POST , instance = user)
        if form.is_valid():
            form.save()
            return redirect('user:index')
        
    
    form = UserForm(instance = user)
    context = {'form': form}
    return render(request, 'user/modifierUser.html', context)   
     

def suprimer (request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('user:index')