from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon1'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon2'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon3', 'type': 'password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon4', 'type': 'password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Ваше имя'
        self.fields['email'].label = 'Электронная почта'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный почтовый адрес уже зарегестрирован в системе')
        return email

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError({'confirm_password': f'Пароли не совпадают'})
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']


class AuthForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon2'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon3', 'type': 'password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Ваша почта'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        us = User.objects.filter(email=self.cleaned_data['email']).first()
        if not us or not authenticate(username=us.username, password=self.cleaned_data['password']):
            raise forms.ValidationError('Неправильный логин или пароль')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'password']


class LKForm(forms.ModelForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon1'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon2'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon3', 'type': 'password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon4', 'type': 'password'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'basic-addon4'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Электронная почта'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['username'].label = 'Ваше имя'
        self.fields['last_name'].label = 'Ваша фамилия'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный почтовый адрес уже зарегестрирован в системе')
        return email

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError({'confirm_password': f'Пароли не совпадают'})
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'username', 'last_name', 'password', 'confirm_password']
