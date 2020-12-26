from django.db import models
from django.conf import settings

class Color(models.Model):
    color_value = models.CharField(unique=True, max_length=50, null=True)

    def __str__(self):
        return self.color_value


class Weight(models.Model):
    weight_value = models.CharField(unique=True, max_length=50, null=True)

    def __str__(self):
        return self.weight_value


class Animal(models.Model):
    SEX_ANIMAL = (
        ('M', 'Кабель'),
        ('Ж', 'Сучка'),
    )
    KIND_ANIMAL = (
        ('С', 'Собака'),
        ('К', 'Кошка'),
    )
    WOOL_ANIMAL = (
        ('К', 'Короткая'),
        ('О', 'Обычная'),
        ('Д', 'Длинная'),
    )
    EARS_ANIMAL = (
        ('С', 'Стоячие'),
        ('П', 'Полустоячие'),
        ('В', 'Висячие'),
        ('К', 'Купированные'),
    )
    TAIl_ANIMAL = (
        ('С', 'Стоячие'),
        ('П', 'Полустоячие'),
        ('В', 'Висячие'),
        ('К', 'Купированные'),
    )
    animal_card = models.CharField(max_length=10, null=True, verbose_name="Номер карточки")
    animal_name = models.CharField(max_length=10, null=True, verbose_name="Кличка")
    animal_kind = models.CharField(max_length=10, choices=KIND_ANIMAL, null=True, verbose_name="Тип")
    animal_gender = models.CharField(max_length=10, choices=SEX_ANIMAL, verbose_name="Пол", null=True)
    animal_color = models.ForeignKey(Color, on_delete=models.CASCADE, max_length=20, null=True, verbose_name="Цвет")
    animal_ears = models.CharField(max_length=20, choices=EARS_ANIMAL, null=True, verbose_name="Уши")
    animal_tail = models.CharField(max_length=20, choices=TAIl_ANIMAL, null=True, verbose_name="Хвост")
    animal_age = models.CharField(max_length=20, null=True, verbose_name="Возраст")
    animal_breed = models.CharField(max_length=50, default='Метис', null=True, verbose_name="Порода")
    animal_size = models.CharField(max_length=10, null=True, verbose_name="Размер")
    animal_weight = models.ForeignKey(Weight, on_delete=models.CASCADE, max_length=20, null=True, verbose_name="Вес")
    animal_wool = models.CharField(max_length=10, choices=WOOL_ANIMAL, null=True, verbose_name="Шерсть")
    area = models.CharField(max_length=2, null=True, verbose_name="Вольер")
    user_id = models.CharField(max_length=10, null=True, verbose_name="Хозяин")
    photo = models.ImageField(upload_to='animals/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.animal_card
