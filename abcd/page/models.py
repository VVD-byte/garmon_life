from django.db import models
from django.contrib.auth.models import User


class Special(models.Model):
    photo = models.ImageField(null=False)
    FIO = models.CharField(max_length=100, null=False)
    info = models.TextField(null=False)
    certificate = models.ImageField(null=False)

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class Work(models.Model):
    name = models.CharField(max_length=100, null=False)
    img = models.ImageField(null=False)
    text = models.TextField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Направление работ'
        verbose_name_plural = 'Направления работ'


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'


class Paper(models.Model):
    slug = models.SlugField(null=False, verbose_name='Идентификатор')
    name = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    small_text = models.TextField(null=False)
    text = models.TextField(null=False)
    like = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Questions(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    quest = models.TextField(null=False)
    date = models.DateTimeField(null=False)
    response = models.TextField(null=True)

    def __str__(self):
        return f'Вопрос от {self.user.email} датировано {self.date}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
