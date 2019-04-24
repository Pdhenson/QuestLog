from django import forms

class QuestForm(forms.Form):
    title_field = forms.CharField(label = "Quest Name", max_length = 30)
    task_field = forms.CharField(label = "Description", max_length = 256)
    step_one = forms.CharField(label = "Step 1", max_length = 255)
    step_two = forms.CharField(label = "Step 2", max_length = 255, required = False)
    step_three = forms.CharField(label = "Step 3", max_length = 255, required = False)
    step_four = forms.CharField(label = "Step 4", max_length = 255, required = False)
    step_five = forms.CharField(label = "Step 5", max_length = 255, required = False)

class SettingsForm(forms.Form):
    check_box = forms.BooleanField()
