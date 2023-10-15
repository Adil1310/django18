from django.urls import path
from .views import MyView, MyTemplateView, MyListView

urlpatterns = [
    path('my-view/', MyView.as_view(), name='my-view'),
    path('my-template-view/', MyTemplateView.as_view(), name='my-template-view'),
    path('my-list-view/', MyListView.as_view(), name='my-list-view')
]