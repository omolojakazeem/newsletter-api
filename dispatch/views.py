from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import LetterDispatcher
from .serializers import LeterDispatchSerializer1, LeterDispatchSerializer2
from subscriber.models import MySubscriber

from .signals import new_dispatch_sent


class LetterDispatchList(generics.GenericAPIView):
    queryset = LetterDispatcher.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LeterDispatchSerializer1
        elif self.request.method == 'POST':
            return LeterDispatchSerializer2
        else:
            return LeterDispatchSerializer1

    def get(self, request, *args, **kwargs):
        dispatch = LetterDispatcher.objects.all()
        serializer_context = {
            'request': request,
        }
        dispatch_serializer = LeterDispatchSerializer1(dispatch, context=serializer_context, many=True)
        dispatch_data = dispatch_serializer.data
        context = {
            'Letter': dispatch_data,
        }
        return Response(context)

    def post(self, request, *args, **kwargs):
        new_dispatch = LeterDispatchSerializer2(data=request.data)
        if new_dispatch.is_valid(raise_exception=True):
            occasion = new_dispatch.validated_data.get('occasion')
            newsletter = new_dispatch.validated_data.get('newsletter')

            new_dispatch_save = new_dispatch.save(occasion=occasion,)

            qs = MySubscriber.objects.all()
            for subscriber in qs:
                recipient_list = new_dispatch_save.receiver_list.add(subscriber)

            new_dispatch_sent.send(
                sender=new_dispatch_save,
                newsletter=newsletter,
                occasion=occasion,
                #receiver_list = recipient_list,
            )

            return Response({
                'Success': f"The newsletter for {new_dispatch_save.occasion} has been successfully sent out"
            })
        return Response({
            'Failed': "Invalid information"
        })


class LetterDispatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LetterDispatcher.objects.all()
    serializer_class = LeterDispatchSerializer1
    #permission_classes = [AllowAny, ]
