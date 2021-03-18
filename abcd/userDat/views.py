from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import AuthForm, RegForm, LKForm
from django.apps import apps
Questions = apps.get_model('page', 'Questions')


def check_login(func):
    def wrap(*args, **kwargs):
        if args[-1].user.is_anonymous:
            return func(*args, **kwargs)
        else:
            return redirect('UserPage')
    return wrap


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('AuthPage')


class UserLK(View):
    def get(self, request):
        if not request.user.is_anonymous:
            return render(request, 'userDat/html/userlkPage.html', context={'name': request.user,
                                                                            'form': LKForm(request.POST or None),
                                                                            'quest': Questions.objects.filter(
                                                                                user__username=request.user)}) # удалить name из context
        return redirect('AuthPage')

    def post(self, request):
        dat = LKForm(request.POST or None)
        if dat.is_valid():
            us = User.objects.filter(username=request.user).first()
            us.first_name = dat.cleaned_data['username']
            us.last_name = dat.cleaned_data['last_name']
            us.password = dat.cleaned_data['password']
            us.save()
            return redirect('UserPage')
        return render(request, 'userDat/html/userlkPage.html', context={'name': request.user,
                                                                        'form': LKForm(request.POST or None),
                                                                        'quest': Questions.objects.filter(
                                                                            user__username=request.user)})  # удалить name из context


class Auth(View):
    @check_login
    def get(self, request):
        return render(request, 'userDat/html/authPage.html', context={'form': AuthForm(request.POST or None)})

    @check_login
    def post(self, request):
        dat = AuthForm(request.POST or None)
        if dat.is_valid():
            us = User.objects.filter(email=dat.cleaned_data['email']).first()
            if us:
                user = authenticate(request, username=us.username, password=dat.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('UserPage')
        return render(request, 'userDat/html/authPage.html', context={'form': AuthForm(request.POST or None)})


class Register(View):
    @check_login
    def get(self, request):
        return render(request, 'userDat/html/register.html', context={'form': RegForm(request.POST or None)})

    @check_login
    def post(self, request):
        data = RegForm(request.POST or None)
        if data.is_valid():
            us = self.generate_username()
            user = User.objects.create_user(username=self.generate_username(), email=data.cleaned_data['email'],
                                            password=data.cleaned_data['password'])
            user.first_name = data.cleaned_data['username']
            user.save()
            user = authenticate(request, username=us, password=data.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('UserPage')
        return render(request, 'userDat/html/register.html', context={'form': RegForm(request.POST or None)})

    def generate_username(self):
        return f'user {User.objects.all().order_by("-id")[0].id}'
