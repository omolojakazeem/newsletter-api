from django.urls import path

from .views import LetterDispatchList, LetterDispatchDetail
urlpatterns = [
    path('',LetterDispatchList.as_view(), name = 'letterdispatcher_list'),
    path('detail/<pk>',LetterDispatchDetail.as_view(), name = 'letterdispatcher_detail'),
]