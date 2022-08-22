from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient
# Register your models here.

User = get_user_model()

class RecipeIngredientsInline(admin.StackedInline):
    model = RecipeIngredient
    extra= 0
    readonly_fields = ['quantity_as_float','as_mks','as_imperial']

class RecipeAdmin(admin.ModelAdmin):
    inlines= [RecipeIngredientsInline]
    list_display = ['name','user']
    readonly_fields= ['timestamp','updated',]
    raw_id_fields = ['user']
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(RecipeIngredient)