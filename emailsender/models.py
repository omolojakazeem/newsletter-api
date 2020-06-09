from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.dispatch import receiver
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from dispatch.signals import new_dispatch_sent

from subscriber.models import MySubscriber


@receiver(new_dispatch_sent)
def new_letter_dispatch(sender, **kwargs):
    dispatch_info = {

        'newsletter': kwargs['newsletter'],
        'occasion': kwargs['occasion'],
    }

    html_message = render_to_string(
        'dispatcher/dispatcher.html',
        {'title': dispatch_info['newsletter'].title,
         'header_content': dispatch_info['newsletter'].header_content,
         'body_content': dispatch_info['newsletter'].body_content,
         'footer_content': dispatch_info['newsletter'].footer_content,
         })
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    emails = MySubscriber.objects.all()

    for email in emails:
        print("email is", email)
        send_mail(
            dispatch_info['newsletter'].title,
            plain_message,
            from_email,
            [email,],
            html_message=html_message,
            fail_silently=False,
        )