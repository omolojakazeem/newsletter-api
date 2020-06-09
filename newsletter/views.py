from django.shortcuts import render
from rest_framework import generics

from .models import MyNewsletter
from .serializers import NewsletterSerializer


class NewsletterList(generics.ListCreateAPIView):
    queryset = MyNewsletter.objects.all()
    serializer_class = NewsletterSerializer
    #permission_classes = [AllowAny, ]


class NewsletterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyNewsletter.objects.all()
    serializer_class = NewsletterSerializer
    #permission_classes = [AllowAny, ]
