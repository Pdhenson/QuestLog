from django import forms

class QuestForm(forms.Form):
    title_field = forms.CharField(label = "Title", max_length = 30)
