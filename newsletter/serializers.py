from rest_framework import serializers

from .models import MyNewsletter


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNewsletter
        fields = '__all__'