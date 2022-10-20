from django.urls import reverse
from django.http import HttpResponse, Http404
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
def recipe_detail_view(request , id=None):
    hx_url = reverse("recipes:hx-detail",kwargs={"id":id})
    context = {
        "hx_url":hx_url,
    }
    return render(request,"recipes/detail.html",context=context)

@login_required
def recipe_detail_hx_view(request , id=None):
    if not request.htmx:
        return Http404
    try:
        my_obj = Recipe.objects.get(id=id,user=request.user)
    except:
        my_obj = None
    if my_obj is None:
        return HttpResponse("Not found.")
    context = {
        "object":my_obj,
    }
    return render(request,"recipes/partials/detail.html",context=context)
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
        if request.htmx:
            header ={
                "hx-Redirect":obj.get_absolute_url()
            }
            return HttpResponse("Created",header=header)
        context['message'] = "Data saved."
        return redirect(obj.get_absolute_url())
    return render(request,"recipes/create-update.html",context=context)
    
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe,id=id,user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)# can u use initial
    new_ingredient_url = reverse("recipes:hx-ingredient-new",kwargs={"parent_id":obj.id})
    context={
        "form":form,
        "object":obj,
        "new_ingredient_url":new_ingredient_url,
    }
    if form.is_valid():
        form.save()
        context['message'] = "updated data."
    if request.htmx:
        return render(request,"recipes/partials/forms.html",context)
    return render(request,"recipes/create-update.html",context)

@login_required
def recipe_ingredient_detail_hx_view(request ,parent_id=None, id=None):
    if not request.htmx:
        return Http404
    try:
        parent_obj = Recipe.objects.get(id= parent_id,user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse("Not found.")
    instance = None
    if id is not None:
        try:
            instance = RecipeIngredient.objects.get(recipe=parent_obj , id= id)
        except:
            instance = None
    form = RecipeIngredientForm(request.POST or None , instance=instance)
    url = instance.get_hx_edit_url() if instance else reverse("recipes:hx-ingredient-new",kwargs={"parent_id":parent_obj.id})
    context = {
        "url":url,
        "form":form,
        "object":instance,
    }
    if form.is_valid():
        new_obj= form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context['object'] = new_obj
        return render(request,"recipes/partials/ingredient-inline.html",context=context)
    return render(request,"recipes/partials/ingredient-form.html",context=context) 