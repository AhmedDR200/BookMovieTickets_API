from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


# 1- without REST and no model query

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