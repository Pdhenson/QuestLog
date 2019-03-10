from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
import json
# Create your views here.

from . import models
from . import forms

def index(request):
    #Form Submission

    if request.method == "POST":
        form_instance = forms.QuestForm(request.POST)
        if form_instance.is_valid():
            new_quest = models.Quest()
            new_quest.title_field = form_instance.cleaned_data["title_field"]
            new_quest.save()
            form_instance = forms.QuestForm()
        else:
            form_instance = forms.QuestForm()
    #Initial Page Load
    form_instance = forms.QuestForm()
    if request.method == "GET":
        print("GET")
    q_list=models.Quest.objects.all()
    n_list = []
    for item in q_list:
        n_list+=[item.title_field + " : " + item.task_field]
    context = {
        "body":"Welcome to the Quest Board!",
        "title":"Assignment 5 Quest Board!",
        "next":"Next",
        "q_list":n_list,
        "form":form_instance
    }
    return render(request, "base.html", context=context)



def quests_json(request):
    i_list = models.Quest.objects.all()
    resp_list = {}
    resp_list["Quests"] = []
    for item in i_list:
        resp_list["Quests"] += [{"QuestName":item.title_field}]
    return JsonResponse(resp_list)
