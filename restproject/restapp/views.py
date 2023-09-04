from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import task
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerialzer
from rest_framework.generics import CreateAPIView

from django.contrib.auth import get_user_model

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    queryset = task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer


class DueViewset(viewsets.ModelViewSet):
    queryset = task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializer


class createuser(CreateAPIView):
    model = get_user_model()
    permission_class = (AllowAny)
    serializer_class = UserSerialzer


class CompletedViewset(viewsets.ModelViewSet):
    queryset = task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializer
