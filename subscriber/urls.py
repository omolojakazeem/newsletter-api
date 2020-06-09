from django.urls import path

from .views import SubscriberList, SubscriberDetail

urlpatterns = [
    path('', SubscriberList.as_view(), name='subscriber_list'),
    path('detail/<int:pk>/', SubscriberDetail.as_view(), name='subscriber_detail'),
]
