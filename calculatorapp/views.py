from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def display(request):
    no1=int(request.post('txtno1'))
    no2=int(request.post('txtno2'))
    v1={'no1':'txtno1','no2':'txtno2'}
    if v1=='add':
        result=no1+no2
    elif v1=='sub':
        result=no1-no2
    else:
        result=no1*no2