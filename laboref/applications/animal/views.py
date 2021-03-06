from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import EditAnimalForm, NewAnimalForm
from .models import Animal


class IndexView(ListView):
    template_name = "animal/index.html"
    model = Animal


def detail_animal_view(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, "animal/detail.html", {'animal': animal})


def edit_animal_view(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    form = EditAnimalForm(initial={
        'animal_name': animal.animal_name,
        'animal_breed': animal.animal_breed,
        'animal_color': animal.animal_color,
        'animal_age': animal.animal_age
    })
    context = {'form': form, 'animal': animal}
    return render(request, "animal/edit.html", context)


def new_animal_view(request):
    if request.method == "POST":
        form = NewAnimalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = NewAnimalForm()
    return render(request, "animal/edit.html", {'form': form})
