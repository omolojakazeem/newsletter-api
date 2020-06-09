from django.dispatch import Signal

new_dispatch_sent = Signal(providing_args=[ "newsletter", "occasion", ])
