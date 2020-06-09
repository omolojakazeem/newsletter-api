from rest_framework import serializers

from .models import MySubscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySubscriber
        fields = '__all__'