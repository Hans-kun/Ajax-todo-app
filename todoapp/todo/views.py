from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from todo.models import  TodoList
from todo.serializers import TodoListSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views 

class HomeView(APIView):


    def get(self, request, format=None):
        todo = TodoList.objects.all()
        serializer = TodoListSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailView(APIView):

    def get_object(self, id):
        try:
            return TodoList.objects.get(id=id)
        except TodoList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        todo = self.get_object(id)
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, id):
        todo = self.get_object(id)
        serializer = TodoListSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo = self.get_object(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def home(request):
#     return render(request, 'todo/index.html', {})