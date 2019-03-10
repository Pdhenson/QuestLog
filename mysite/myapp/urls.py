from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('quests/', views.quests_json),
]
