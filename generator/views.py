from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request,'generator/home.html')

def password(request):
    character=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        character.extend(list('0123456789'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_+'))

    length=int(request.GET.get('length',12))
    the_password=''
    for x  in range(length):
        the_password+=random.choice(character)
    return render(request,'generator/password.html',{'password':the_password})

def web_info(request):
    return render(request,'generator/info.html')
