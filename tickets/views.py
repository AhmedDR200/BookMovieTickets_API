from django.http import JsonResponse
from django.shortcuts import render
from .models import Guest , Movie , Reservation

# Create your views here.


# 1- no REST and no model query

def no_rest_no_model(request):
    guests = [
        {
        'id':1,
        'name':"ahmed",
        'mobile': '01097215012',
    },
    {
        'id':2,
        'name':"wali",
        'mobile': '01117473045',
    }

    ]

    return JsonResponse(guests, safe=False)


# 2- no REST from model

def no_rest_from_model(request):
    data= Guest.objects.all()
    response = {
        "data": list(data.values('name', 'mobile')),
    }
    return JsonResponse(response)