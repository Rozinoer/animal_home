from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, AnimalRegistrationForm, AnimalEditForm, \
    ShelterRegistrationForm, ShelterEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Shelter
from shelter.models import Animal
from django.contrib.auth.models import User


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return render(request, 'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        img = request.user.profile.photo
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,
                       'img': img})


@login_required
def animal_edit(request):
    animal = Animal.objects.filter(id=1).first()
    print(animal)
    if request.method == 'POST':
        animal_form = AnimalEditForm(instance=animal, data=request.POST)
        if animal_form.is_valid():
            animal_form.save()
        return render(request, 'account/animal_edit.html',
                      {'user_form': animal_form, })
    else:
        animal_form = AnimalEditForm(instance=animal)
        return render(request,
                      'account/animal_edit.html',
                      {'user_form': animal_form})


@login_required
def edit_shelter(request):
    shelter = Shelter.objects.filter(user=request.user).first()
    print(shelter)
    if request.method == 'POST':
        shelter_form = ShelterEditForm(instance=shelter, data=request.POST)
        if shelter_form.is_valid():
            shelter_form.save()
        return render(request, 'account/shelter_edit.html',
                      {'user_form': shelter_form, })
    else:
        shelter_form = ShelterEditForm(instance=shelter)
        return render(request,
                      'account/shelter_edit.html',
                      {'shelter_form': shelter_form})


def logged_out(request):
    return render(request, 'registration/logged_out.html')


@login_required
def dashboard(request):
    img = request.user.profile.photo
    return render(request, 'account/dashboard.html', {'section': 'dashboard',
                                                      'img': img})


@login_required
def self_page(request):
    animal_list = Animal.objects.filter(user_id=request.user)
    shelter_list = Shelter.objects.filter(user=request.user)
    # user = User.objects.filter(username=request.user)
    context = {
        'user_name': request.user.first_name,
        'user_second_name': request.user.last_name,
        'animal_list': animal_list,
        'shelter_list': shelter_list
    }
    return render(request, 'account/account.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def register_animal(request):
    if request.method == 'POST':
        animal_form = AnimalRegistrationForm(request.POST)
        if animal_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_animal = animal_form.save(commit=False)
            new_animal.user_id = request.user
            # Set the chosen password
            # Save the User object
            new_animal.save()
            # profile = Animal.objects.create(user=new_animal)
            return render(request, 'account/register_animal_done.html')
    else:
        animal_form = AnimalRegistrationForm()
    return render(request, 'account/add_animal.html', {'animal_form': animal_form})


@login_required
def register_shelter(request):
    if request.method == 'POST':
        shelter_form = ShelterRegistrationForm(request.POST)
        if shelter_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_shelter = shelter_form.save(commit=False)
            new_shelter.user = request.user
            # Set the chosen password
            # Save the User object
            new_shelter.save()
            # profile = Animal.objects.create(user=new_animal)
            return render(request, 'account/register_animal_done.html')
    else:
        shelter_form = ShelterRegistrationForm()
    return render(request, 'account/add_shelter.html', {'shelter_form': shelter_form})
