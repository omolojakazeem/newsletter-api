from rest_framework import serializers

from .models import LetterDispatcher


class LeterDispatchSerializer1(serializers.ModelSerializer):
    class Meta:
        model = LetterDispatcher
        fields = '__all__'


class LeterDispatchSerializer2(serializers.ModelSerializer):
    class Meta:
        model = LetterDispatcher
        fields = ['occasion','newsletter']
