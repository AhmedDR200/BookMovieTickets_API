from django.http import Http404
from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest , Movie , Reservation
from rest_framework.decorators import api_view
from .serializers import GustSerializer , MovieSerializer , ReservationSerializer
from rest_framework import status , filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics , mixins , viewsets


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



@api_view(['GET','PUT','DELETE'])
def fbv_detail(request,pk):
     #GET  
    try:  
     gust = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = GustSerializer(gust) #many for multiple objects in one time
        return Response(serializer.data)

     #PUT
    elif request.method =='PUT':
        serializer = GustSerializer(gust,data=request.data) #create object
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
     #DELETE  
    if request.method =='DELETE':
        gust.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# ======================================================

# 4- class based view
# 4.1- LIST , CREATE == GET , POST

class CBV_List(APIView):
    def get (self,request):
        guests = Guest.objects.all()
        serializer = GustSerializer(guests , many= True) #many for multiple objects in one time
        return Response(serializer.data )
    
    def post (self,request):
        serializer = GustSerializer(data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# 4.2- GET , PUT , DELETE (pk)

class CBV_Detail(APIView):
    def get_object (self, pk ):
        try:
            return Guest.objects.get(pk=pk) #get by id

        except Guest.DoesNotExist:
         raise Http404("Guest does not exist")
        

    def get (self,request, pk ):
        guest = self.get_object(pk)
        serializer = GustSerializer(guest)
        return Response(serializer.data)
    

    def put (self,request, pk):
        geust = self.get_object(pk)
        serializer = GustSerializer(geust, data=request.data) #update the object with new values
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) #no content means deleted successfully


# 5- MIXINS
# 5.1- mixins list

class Mixins_list(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
 ):
    queryset = Guest.objects.all()
    serializer_class = GustSerializer

    def get(self,request):
        return self.list(request) #list method is inherited from ModelListMixin
    
    def post(self,request):
        return self.create(request) # create method is inherited from CreateModelMixin
    


# 5.2- mixins GET , PUT , DELETE

class Mixins_Detail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Guest.objects.all()
    serializer_class = GustSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk) # retrieve method is inherited from RetrieveModelMixin
    
    def put(self, request, pk):
        return self.update(request, pk) # update method is inherited from UpdateModelMixin
    
    def delete(self, request, pk):
        return self.destroy(request, pk) # destroy method is inherited from DestroyModelMixin
    




# 6- generics
# 6.1- GET , POST

class Generics_List(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GustSerializer


# 6.2- GET , PUT , DELETE
class Generics_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GustSerializer





# 7- ViewSets

class ViewSets_Geust(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GustSerializer





# =========================================================================================

