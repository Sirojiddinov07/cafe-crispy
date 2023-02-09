from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log
def index(request):
    context = {
        'foods': Foods.objects.all(),
        'goods': Foods.objects.filter(rating=5).order_by('-id')[:2],
        'news': News.objects.all()
    }
    return render(request, 'index.html', context)



def about(request):

    contex = {
        'about': About.objects.last(),
        'team': Team.objects.all().order_by('-id')[:3],
    }
    return render(request, 'about.html', contex)



def contact(request):
    if request.method =='POST':
        name = request.POST['contact-name']
        phone = request.POST['contact-phone']
        email = request.POST['contact-email']
        message = request.POST['contact-message']
        Contact.objects.create(name=name, phone=phone, email=email, message=message)
    return render(request, 'contact.html')



def menu(request):
    contex = {
        'foods': Foods.objects.all(),
    }
    return render(request, 'menu.html', contex)


def news(request):
    contex = {
        'news': News.objects.all()

    }
    return render(request, 'news.html', contex)


def news_detail(request, pk):
    contex = {
        'news': News.objects.filter(id=pk),
        'rel_news': News.objects.all().order_by('-id')[:3],
    }
    return render(request, 'news-detail.html', contex)



def food_detail(request, pk):
    contex = {
        'food': Foods.objects.filter(id=pk),
        'team': Team.objects.all(),
    }
    return render(request, 'foods-detail.html', contex)



def team_detail(request, pk):
    contex = {
        'team': Team.objects.filter(id=pk),
    }
    return render(request, 'team-detail.html', contex)


def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            log(request, user)
            return redirect('index')
        else:
            return redirect('login_user')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login_user')

def reserve(request):

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        people = request.POST['people']
        date = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']
    Reserve.objects.create(full_name=name, email=email, phone=phone,
                           num_person=people, date=date,
                           time=time, request=message)
    return redirect('index')




def register(request):
    form = CreateUserForm()

    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('index')


        # form = CreateUserForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('index')
        # else:
        #     return redirect('login_user')

    return render(request, 'register.html', {'form':form})

