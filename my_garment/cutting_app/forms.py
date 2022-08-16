from distutils.command.clean import clean
from django.forms import ModelChoiceField
from django import forms
from django.shortcuts import get_object_or_404
from django.core.validators import validate_email
from .models import Stock
from django.core.exceptions import ValidationError
from cutting_app.models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','slug','content','publish']
        Widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'})
        }
        
    # def clean(self):
    #     data = self.cleaned_data
    #     title = data.get("title")
    #     if title != None:
    #         qs = Articles.objects.all().filter(title__icontains=title)
    #     if qs.exists():
    #         self.add_error("title",f" \"{title}\" already in use .")
    #     return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    # def clean_title(self): 
    #     cleaned_data = self.cleaned_data
    #     print("cleaned_data",cleaned_data)
    #     title = cleaned_data.get("title")
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('This title is taken. ')
    #     print("title",title)
    #     return title
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "the office":
            self.add_error("title",f" the {title} title was taken .")
        if "office" in content or "office" in title:
            raise forms.ValidationError("office is not allowed .")
        return cleaned_data


class StockForm(forms.Form):
    stock_id= forms.IntegerField()
    stock_name=forms.CharField()
    notes = forms.CharField()
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        stock_id = cleaned_data.get("stock_id")
        if stock_id == int("2"):
            self.add_error("stock_id","this id was taken. ")
        return cleaned_data
    # class Meta:
    #     model = Stock
    #     fields = [
    #         'stock_id',
    #         'stock_name',
    #         # 'emp_id',
    #         'note',
    #     ]

    #     widgets = {
    #         'stock_id':forms.NumberInput(attrs={'class':'form-control' ,'name':'emp_name'}),
    #         'stock_name':forms.TextInput(attrs={'class':'form-control' ,'name':'emp_name'}),
    #         # 'emp_id':tableSelect(attrs={'class':'form-control' ,'name':'emp_name'}),
    #         'note':forms.Textarea(attrs={'class':'form-control' ,'name':'emp_name'}),
            

    #     }