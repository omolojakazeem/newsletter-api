from django.urls import path

from .views import NewsletterList, NewsletterDetail

urlpatterns = [
    path('', NewsletterList.as_view(), name='newsletter_list'),
    path('detail/<pk>', NewsletterDetail.as_view(), name='newsletter_detail'),
]
