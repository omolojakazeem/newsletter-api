from django.conf import settings
from django.db import models

from newsletter.models import MyNewsletter

from subscriber.models import MySubscriber


class LetterDispatcher(models.Model):
    receiver_list = models.ManyToManyField(MySubscriber, related_name='letter_dispatcher')
    occasion = models.CharField(max_length=50)
    newsletter = models.ForeignKey(MyNewsletter,on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.occasion

