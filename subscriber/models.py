from django.db import models

SUBSCRIBER_STATUS = (
    ('ACTIVE', 'ACTIVE'),
    ('DEACTIVE', 'DEACTIVE')
)


class MySubscriber(models.Model):
    email = models.EmailField()
    status = models.CharField(choices=SUBSCRIBER_STATUS, default='ACTIVE', max_length=10)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
