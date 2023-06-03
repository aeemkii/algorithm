from django.db import models

# Create your models here.

class Questions(models.Model):
    question = models.TextField("Вопрос")
    answer = models.TextField("Ответ")


class Category(models.Model):
    name = models.CharField("Название", max_length=255)
    image = models.ImageField("Фотография", upload_to='photo')
    slug = models.SlugField(max_length=70, unique=True)


class Services(models.Model):
    name = models.CharField("Название", max_length=255)
    category = models.ForeignKey(Category, max_length=150, on_delete=models.CASCADE)


class AboutUs(models.Model):
    description = models.TextField("Описание")
    image = models.ImageField("Фотография", upload_to='photo')


class Team(models.Model):
    description = models.TextField("Описание")
    image = models.ImageField("Фотография", upload_to='photo')


class Information(models.Model):
    name = models.TextField("ФИО")
    position = models.TextField("Должность")
    description = models.TextField("Описание")
    image = models.ImageField("Фотография", upload_to='photo')


class Contacts(models.Model):
    email = models.CharField("Почта", max_length=255)
    requisites = models.CharField("Реквизиты компании", max_length=255)
    inn = models.IntegerField("ИНН")
    okpo = models.CharField("ОКПО компании", max_length=255)
    address = models.TextField("Адрес")
    phone = models.CharField("Номер телефона", max_length=18)