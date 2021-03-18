from django import forms


class QuestForm(forms.Form):
    quest = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon3'}), label='Вопрос')

