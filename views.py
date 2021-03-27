from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'complaintboard/index.html')

def signup(request):
    return render(request,'complaintboard/signup.html')

def fac(request):
    return render(request,'complaintboard/fac.html')

def login(request):
    return render(request,'complaintboard/login.html')

def logined(request):
    username_ = request.POST.get('username')
    pass_ = request.POST.get('password_')
    params = {'username':username_ ,'password__' : pass_}
    return render(request,'complaintboard/mypage.html',params)