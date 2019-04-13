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
    quest_list=models.Quest.objects.all()

    n_list = []
    for item in quest_list:
        n_list = [item.title_field]
    context = {
        "body":"Welcome to the Quest Board!",
        "title":"Assignment 5 Quest Board!",
        "next":"Next",
        "n_list":n_list,
        "form":form_instance
    }
    return render(request, "base.html", context=context)

def newQ(request):
    #Form Submission



    q_list = models.Quest.objects.all()
    s_list = models.Steps.objects.all()

    multi_list = []
    title_list = []
    task_list = []
    step1_list = []
    step2_list = []
    step3_list = []
    step4_list = []
    step5_list = []



    for i in range(0,2):
        for item in q_list:
            if i == 0:
                title_list.append([item.title_field])
            elif i == 1:
                task_list.append([item.task_field])

    for j in range(0,5):
        for item2 in s_list:
            if j == 0:
                step1_list.append([item2.step_one])
            elif j == 1:
                step2_list.append([item2.step_two])
            elif j == 2:
                step3_list.append([item2.step_three])
            elif j == 3:
                step4_list.append([item2.step_four])
            elif j == 4:
                step5_list.append([item2.step_five])


        multi_list = zip(title_list, task_list, step1_list, step2_list, step3_list, step4_list, step5_list)

    context = {
        "body":"Welcome to the Quest Board!",
        "title":"Assignment 5 Quest Board!",
        "next":"Next",
        "multi_list":multi_list,

    }
    return render(request, "newQ.html", context=context)

def quests_json(request):
    i_list = models.Quest.objects.all()
    resp_list = {}
    resp_list["Quests"] = []
    for item in i_list:
        resp_list["Quests"] += [{"QuestName":item.title_field}]
    return JsonResponse(resp_list)

def post_quest(request):
    if request.method == "POST":
        form_instance = forms.QuestForm(request.POST)
        if form_instance.is_valid():
            new_quest = models.Quest()
            new_steps = models.Steps()
            new_quest.title_field = form_instance.cleaned_data["title_field"]
            new_steps.title_field = form_instance.cleaned_data["title_field"]
            new_quest.task_field = form_instance.cleaned_data["task_field"]
            new_steps.step_one = form_instance.cleaned_data["step_one"]
            new_steps.step_two = form_instance.cleaned_data["step_two"]
            new_steps.step_three = form_instance.cleaned_data["step_three"]
            new_steps.step_four = form_instance.cleaned_data["step_four"]
            new_steps.step_five = form_instance.cleaned_data["step_five"]
            new_steps.save()
            new_quest.save()
            form_instance = forms.QuestForm()
        else:
            form_instance = forms.QuestForm()
    #Initial Page Load
    form_instance = forms.QuestForm()
    if request.method == "GET":
        print("GET")

    context = {
        "form":form_instance
    }
    return render(request, "AddQuest.html", context=context)
