from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest , Movie , Reservation
from rest_framework.decorators import api_view
from .serializers import GustSerializer , MovieSerializer , ReservationSerializer
from rest_framework import status , filters
from rest_framework.response import Response


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

# =========================================================


# list items --> GET
# create item --> POST
# ================================
# pk quiery (1 item) --> GET
# update --> PUT
# delete --> DELETE

# 3- function based views
# 3.1- GET POST
@api_view(['GET','POST'])
# GET
def fbv_list(request):
    if request.method =='GET':
        guests = Guest.objects.all() #quiery set
        serializer = GustSerializer(guests , many=True ) #many for multiple objects in one time
        return Response(serializer.data)

#POST
    elif request.method =='POST':
        serializer = GustSerializer(data=request.data) #create object
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

