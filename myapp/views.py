from django.shortcuts import render
from .models import Drink
from .serielizers import DrinkSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from myapp import serielizers

# Create your views here.
@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drinkdetail(request, pk, format=None):
    try:
        drink = Drink.objects.get(id=pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serielizer = DrinkSerializer(drink)
        return Response(serielizer.data)

    elif request.method == 'PUT':
        serielizer = DrinkSerializer(drink, data=request.data)
        if serielizer.is_valid():
            serielizer.save()
            return Response(serielizer.data)
        return Response(serielizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "Delete":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

