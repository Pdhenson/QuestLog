from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('newQ', views.newQ),
    path('myQ', views.myQ),
    path('PostQuest', views.post_quest),
    path('quests/', views.quests_json),
]
