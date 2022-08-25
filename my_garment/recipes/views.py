from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect, get_object_or_404
from .models import Recipe,RecipeIngredient
from django.forms.models import modelformset_factory # models form for querysets
from .forms import RecipeForm, RecipeIngredientForm
# Create your views here.
# CRUD -> Create Retrieve Update & Delete


@login_required 
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        "object_list":qs,
    }
    return render(request,"recipes/list.html",context)

@login_required
def recipe_detail_view(request , id=id):
    obj = get_object_or_404(Recipe,id=id,user=request.user)
    context = {
        "object":obj,
    }
    return render(request,"recipes/detail.html",context)

def recipe_create_view(request):
    context = {
        "form":RecipeForm()
    }
    form = RecipeForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        context['message'] = "Data saved."
        return redirect(obj.get_absolute_url())
    return render(request,"recipes/create-update.html",context=context)
    


def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe,id=id,user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)# can u use initial
    # form_2 = RecipeIngredientForm(request.POST or None)
    RecipeIngredientFormset = modelformset_factory(RecipeIngredient,form=RecipeIngredientForm,extra=0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormset(request.POST or None , queryset=qs)
    context={
        "form":form,
        "formset":formset,
        "object":obj,
    }
    if request.method== "POST":
        print(request.POST)
    if  all([form.is_valid() and formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form_2 in formset:
            child = form_2.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = "updated data."
    return render(request,"recipes/create-update.html",context)