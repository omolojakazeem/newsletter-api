from django.shortcuts import render
from rest_framework import generics

from .models import MySubscriber
from .serializers import SubscriberSerializer


class SubscriberList(generics.ListCreateAPIView):
    queryset = MySubscriber.objects.all()
    serializer_class = SubscriberSerializer
    #permission_classes = [AllowAny, ]


class SubscriberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MySubscriber.objects.all()
    serializer_class = SubscriberSerializer
    #permission_classes = [AllowAny, ]
