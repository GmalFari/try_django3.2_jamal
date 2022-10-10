from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    required_css_class="required-field"
    error_css_class = "error-field"
    name = forms.CharField(help_text="This is help text <a href='#'>contact us </a>")
    class Meta:
        model = Recipe
        fields=['name','description', 'directions']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            new_data = {
                "placeholder":f"Recipe {str(field)}",
                "class":"form-control",
                # "hx-post":".",
                # "hx-trigger":"keyup changed delay:500ms",
                # "hx-target":"#recipe-containter",
                # "hx-swap":"outerHTML",
                }
            self.fields[str(field)].widget.attrs.update(new_data)
        self.fields['description'].widget.attrs.update({"rows":'2'})
        self.fields['directions'].widget.attrs.update({"rows":'4'})
        # self.fields['name'].widget.attrs.update({"class":"form-control-2"})
    

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']