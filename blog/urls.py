from django.urls import path

from . import views
urlpatterns = [
    path('page<int:page>', views.allblogs, name="allblogs"),
    path('<str:slug>/', views.detail, name='detail')
    ]

