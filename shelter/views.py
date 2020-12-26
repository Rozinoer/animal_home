from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Animal, Color, Weight


# from .forms import AnimalRegistrationForm


def index(request):
    animal_list = Animal.objects.all()
    context = {
        'animal_list': animal_list
    }
    return render(request, 'shelter/main.html', context)


def search_page(request):
    animal_list = Animal.objects.all()
    # img = request.animal.photo
    color_list = Color.objects.all()
    weight_list = Weight.objects.all()
    context = {
        'animal_list': animal_list,
        'color_list': color_list,
        'weight_list': weight_list
    }
    return render(request, 'shelter/pets.html', context)


def send_query(request):
    animal_list = Animal.objects.all()
    color_list = Color.objects.all()
    if request.POST['color'] != 'None':
        for color in color_list:
            if color.color_value == request.POST['color']:
                color_id = color.id
                break
        animal_list = Animal.objects.filter(animal_color=color_id)
    if request.POST['ears'] != 'None':
        animal_list = Animal.objects.filter(animal_ears=request.POST['ears'])
    if request.POST['size'] != 'None':
        animal_list = Animal.objects.filter(animal_size=request.POST['size'])
    if request.POST['age'] != 'None':
        animal_list = Animal.objects.filter(animal_age=request.POST['age'])
    # if request.POST['weight'] != 'None':
    #     animal_list = Animal.objects.filter(animal_ears=request.POST['weight'])
    if request.POST['breed'] != 'None':
        animal_list = Animal.objects.filter(animal_breed=request.POST['breed'])
    if request.POST['wool'] != 'None':
        animal_list = Animal.objects.filter(animal_wool=request.POST['wool'])
    if request.POST['tail'] != 'None':
        animal_list = Animal.objects.filter(animal_tail=request.POST['tail'])
    return animal_list


def search_filter(request):
    weight_list = Weight.objects.all()
    color_list = Color.objects.all()
    if request.method == 'POST':
        animal_list = send_query(request)
        context = {
            'animal_list': animal_list,
            'weight_list': weight_list,
            'color_list': color_list
        }
        return render(request, 'shelter/pets.html', context)
