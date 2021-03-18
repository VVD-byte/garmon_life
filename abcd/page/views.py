from django.shortcuts import render, redirect
from django.views import View
from .models import Special, Category, Paper, Work, Questions
from .forms import QuestForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.http import Http404


def check_login(func):
    def wrap(*args, **kwargs):
        if not args[-1].user.is_anonymous:
            return func(*args, **kwargs)
        else:
            return redirect('UserPage')
    return wrap


class Main(View):
    def get(self, request):
        return render(request, 'page/html/mainPage.html')

    def post(self, request):
        pass


class Paper_(View):
    def get(self, request):
        return render(request, 'page/html/paper.html', context={'left_menu': Category.objects.all(), 'data': Paper.objects.all()})

    def post(self, request):
        pass


class PaperSlug(View):
    def get(self, request, slug):
        dat = Paper.objects.filter(slug=slug)[0]
        return render(request, 'page/html/paper_slug.html', context={'data': dat, 'text': mark_safe(dat.text), 'user': request.user})

    def post(self, request):
        pass


class PaperNew(View):
    def get(self, request):
        if request.user.is_superuser:
            return render(request, 'page/html/paper_new.html')
        else:
            raise Http404

    def post(self, request):
        pass


class Spec(View):
    def get(self, request):
        return render(request, 'page/html/specialise.html', context={'spec': Special.objects.all()})

    def post(self, request):
        pass


class Work_(View):
    def get(self, request):
        return render(request, 'page/html/Work.html', context={'work': Work.objects.all()})

    def post(self, request):
        pass


class Quest(View):
    def get(self, request):
        return render(request, 'page/html/questions.html', context={'quest': Questions.objects.filter(response__isnull=False),
                                                                    'form': QuestForm(), 'user': request.user.is_anonymous})

    @check_login
    def post(self, request):
        dat = QuestForm(request.POST or None)
        if dat.is_valid():
            Questions(user=User.objects.filter(username=request.user).first(), quest=dat.cleaned_data['quest'],
                      date=timezone.now()).save()
        return self.get(request)
