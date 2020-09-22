# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets  # add this
from .serializers import ThingstodoSerializer  # add this
from .models import Thingstodo  # add this


class TodoView(viewsets.ModelViewSet):  # add this
    serializer_class = ThingstodoSerializer  # add this
    queryset = Thingstodo.objects.all()  # add this
