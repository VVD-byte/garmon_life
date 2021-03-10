from django import forms


class QuestForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon1'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon2'}))
    quest = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon3'}), label='Вопрос')
