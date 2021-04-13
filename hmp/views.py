from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from hmp.forms import RegistrationForm,ClassForm,ImageForm,ImageProtoForm,InsertForm
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.views.decorators.cache import cache_control, never_cache
from django.contrib import messages
from simple_search import search_filter
from .models import Plant,PlantInfo
from django.db.models.query import QuerySet
from django.template.defaultfilters import length
from hmp.utils import *
from hmp.models import *
import itertools
from pip._internal.cli.cmdoptions import no_cache



 
@never_cache
def index(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        print(request.user)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            return redirect('home.html')             
    else:
        if request.user.is_authenticated:
            return redirect('home.html')
        form=AuthenticationForm()
        return render(request,'index.html',{'form':form})
        print(request.user)
        

@login_required
def admin(request):
    args={'user':request.user}
    return render(request,'admin.html',args)

@login_required
@cache_control(must_revalidate=True,no_store=True)
def editprofile(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'editprofile.html', {'form': form})


@login_required(login_url='index')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def home(request):
        return HttpResponse(render(request,'home.html'))

@login_required
@cache_control(must_revalidate=True)
def insertpage(request):
    if request.method=='POST':
        form=InsertForm(request.POST,request.FILES)     
        print("just outside form validation")
        if form.is_valid():
            print("Inside form validation")
            form.save()
            return redirect('home.html')
    else:
        form=InsertForm()
        return render(request,'insertpage.html',{'form':form})

@login_required
@cache_control(must_revalidate=True,no_store=True)
def modifypage(request,oid):
    '''plantInfo=getPlantInfo(oid)'''
    plant=Plant.objects.get(plant_id=oid)
    form=InsertForm(request.POST or None, instance= plant)
    return render(request,'modifypage.html',{'form': form})

@login_required
@cache_control(must_revalidate=True)
def results(request,oid,plant_name):
    print(oid)
    plantInfo=getPlantInfo(oid)
    return render(request,'results.html',{'plantInfo':plantInfo})

@login_required
@cache_control(must_revalidate=True)
def searchresults(request):
    searchBy = request.GET['o']
    print(searchBy)
    query=request.GET['q']
    query=query.strip()
    print(query)
    plantsInfo=search(query,searchBy)
    return render(request,'searchresults.html',{'plantsInfo':plantsInfo})

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            return redirect('home.html')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('index')



