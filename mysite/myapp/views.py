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
        "form":form_instance,

    }
    return render(request, "base.html", context=context)

def newQ(request):
    #Form Submission
    user = request.user
    if request.method == 'POST':
        values = request.POST.get('idNum')
        print(values)
        updateUser = models.Quest.objects.filter(id = values)

        #Set the quests User to the current user
        models.Quest.objects.filter(id = values).update(user_name= str(user))

        #Set the steps User to the current user
        models.Steps.objects.filter(quest_id = values).update(user_name= str(user))


    q_list = models.Quest.objects.all().exclude(user_name= str(user))
    s_list = models.Steps.objects.all().exclude(user_name= str(user))

    multi_list = []
    title_list = []
    titleId = []
    task_list = []
    stepId = []
    step1_list = []
    step2_list = []
    step3_list = []
    step4_list = []
    step5_list = []

    for i in range(0,2):
        for item in q_list:
            if i == 0:
                title_list.append([item.title_field])
                titleId.append(item.id)
            elif i == 1:
                task_list.append([item.task_field])

    for j in range(0,5):
        for item2 in s_list:
            if j == 0:
                step1_list.append([item2.step_one])
                stepId.append(item2.id)
            elif j == 1:
                step2_list.append([item2.step_two])
            elif j == 2:
                step3_list.append([item2.step_three])
            elif j == 3:
                step4_list.append([item2.step_four])
            elif j == 4:
                step5_list.append([item2.step_five])


        multi_list = zip(title_list, task_list, step1_list, step2_list, step3_list, step4_list, step5_list, titleId, stepId)

    context = {
        "body":"Welcome to the Quest Board!",
        "title":"Assignment 5 Quest Board!",
        "next":"Next",
        "multi_list":multi_list,

    }
    return render(request, "newQ.html", context=context)

def myQ(request):
    #Form Submission

    user = request.user
    q_list = models.Quest.objects.all().filter(user_name= str(user))
    s_list = models.Steps.objects.all().filter(user_name= str(user))

    if request.method == 'POST':
        value1 = request.POST.get('checkbox1One')
        value0 = request.POST.get('checkbox1Zero')

        value2 = request.POST.get('checkbox2One')
        value3 = request.POST.get('checkbox2Zero')

        value4 = request.POST.get('checkbox3One')
        value5 = request.POST.get('checkbox3Zero')

        value6 = request.POST.get('checkbox4One')
        value7 = request.POST.get('checkbox4Zero')

        value8 = request.POST.get('checkbox5One')
        value9 = request.POST.get('checkbox5Zero')

        if value0 is not None:
            s_list.filter(quest_id = value0).update(completion_percent = ( s_list.get(quest_id = value0).completion_percent - 1))
            s_list.filter(quest_id = value0).update(step_one_complete= 0)
        if value1 is not None:
            s_list.filter(quest_id = value1).update(completion_percent = ( s_list.get(quest_id = value1).completion_percent + 1))
            s_list.filter(quest_id = value1).update(step_one_complete= 1)

        if value2 is not None:
            s_list.filter(quest_id = value2).update(completion_percent = ( s_list.get(quest_id = value2).completion_percent + 1))
            s_list.filter(quest_id = value2).update(step_two_complete= 1)
        if value3 is not None:
            s_list.filter(quest_id = value3).update(completion_percent = ( s_list.get(quest_id = value3).completion_percent - 1))
            s_list.filter(quest_id = value3).update(step_two_complete= 0)

        if value4 is not None:
            s_list.filter(quest_id = value4).update(completion_percent = ( s_list.get(quest_id = value4).completion_percent + 1))
            s_list.filter(quest_id = value4).update(step_three_complete= 1)
        if value5 is not None:
            s_list.filter(quest_id = value5).update(completion_percent = ( s_list.get(quest_id = value5).completion_percent - 1))
            s_list.filter(quest_id = value5).update(step_three_complete= 0)

        if value6 is not None:
            s_list.filter(quest_id = value6).update(completion_percent = ( s_list.get(quest_id = value6).completion_percent + 1))
            s_list.filter(quest_id = value6).update(step_four_complete= 1)
        if value7 is not None:
            s_list.filter(quest_id = value7).update(completion_percent = ( s_list.get(quest_id = value7).completion_percent - 1))
            s_list.filter(quest_id = value7).update(step_four_complete= 0)

        if value8 is not None:
            s_list.filter(quest_id = value8).update(completion_percent = ( s_list.get(quest_id = value8).completion_percent + 1))
            s_list.filter(quest_id = value8).update(step_five_complete= 1)
        if value9 is not None:
            s_list.filter(quest_id = value9).update(completion_percent = ( s_list.get(quest_id = value9).completion_percent - 1))
            s_list.filter(quest_id = value9).update(step_five_complete= 0)

    multi_list = []
    multi_checkbox = []
    title_list = []
    titleId = []
    task_list = []
    stepId = []
    step1_list = []
    step2_list = []
    step3_list = []
    step4_list = []
    step5_list = []
    completion_percent_list = []

    step1_bool_list = []
    step2_bool_list = []
    step3_bool_list = []
    step4_bool_list = []
    step5_bool_list = []

    percTotal = 0
    percTotal_list = []


    for i in range(0,2):
        for item in q_list:
            if i == 0:
                title_list.append(item.title_field)
                titleId.append(item.id)
            elif i == 1:
                task_list.append(item.task_field)


    for j in range(0,6):
        for item2 in s_list:
            percTotal = 0
            if j == 0:
                step1_list.append(item2.step_one)
                stepId.append(item2.id)
                step1_bool_list.append(item2.step_one_complete)
            elif j == 1:
                step2_bool_list.append(item2.step_two_complete)
                if item2.step_two is "":
                    step2_list.append("NA")
                else:
                    step2_list.append(item2.step_two)
            elif j == 2:
                step3_bool_list.append(item2.step_three_complete)
                if item2.step_three is "":
                    step3_list.append("NA")
                else:
                    step3_list.append(item2.step_three)
            elif j == 3:
                step4_bool_list.append(item2.step_four_complete)
                if item2.step_four is "":
                    step4_list.append("NA")
                else:
                    step4_list.append(item2.step_four)
            elif j == 4:
                step5_bool_list.append(item2.step_five_complete)
                if item2.step_five is "":
                    step5_list.append("NA")
                else:
                    step5_list.append(item2.step_five)
            elif j == 5:
                completion_percent_list.append(item2.completion_percent)
            if item2.step_one != None and item2.step_one != "" and item2.step_one != "NA":
                percTotal += 1;
            if item2.step_two != None and item2.step_two != "" and item2.step_two != "NA":
                percTotal += 1;
            if item2.step_three != None and item2.step_three != "" and item2.step_three != "NA":
                percTotal += 1;
            if item2.step_four != None and item2.step_four != "" and item2.step_four != "NA":
                percTotal += 1;
            if item2.step_five != None and item2.step_five != "" and item2.step_five != "NA":
                percTotal += 1;
            print(percTotal)
            percTotal_list.append(percTotal)


    print(percTotal_list)


    multi_list = zip(title_list, task_list, step1_list, step2_list, step3_list, step4_list, step5_list, titleId, completion_percent_list, step1_bool_list, step2_bool_list, step3_bool_list, step4_bool_list, step5_bool_list, percTotal_list)

    context = {
        "body":"Welcome to the Quest Board!",
        "title":"Assignment 5 Quest Board!",
        "next":"Next",
        "multi_list":multi_list,
        "multi_checkbox":multi_checkbox,
        "NA":"NA",
        "percTotal":percTotal




    }

    return render(request, "myQ.html", context=context)

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
            new_quest.title_field = form_instance.cleaned_data["title_field"]
            new_quest.task_field = form_instance.cleaned_data["task_field"]
            new_quest.save()
            print(new_quest.id)
            new_steps = models.Steps()
            print(new_steps.quest_id)
            new_steps.quest_id = new_quest.id
            new_steps.title_field = form_instance.cleaned_data["title_field"]
            new_steps.step_one = form_instance.cleaned_data["step_one"]
            new_steps.step_two = form_instance.cleaned_data["step_two"]
            new_steps.step_three = form_instance.cleaned_data["step_three"]
            new_steps.step_four = form_instance.cleaned_data["step_four"]
            new_steps.step_five = form_instance.cleaned_data["step_five"]
            new_steps.save()
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
