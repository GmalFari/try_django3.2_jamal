from socket import fromshare
from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.Form):
    class Meta:
        model = Recipe
        fields=['name','description', 'directions']
    
