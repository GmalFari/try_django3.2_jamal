
from django.shortcuts import redirect, HttpResponse ,render,HttpResponseRedirect,get_object_or_404 ,redirect,Http404
from django.contrib.auth.decorators import login_required
from . import models
from . import myclass

from .models import Articles,Stock
from .forms import  ArticleForm,StockForm
from django.urls import reverse
from django.apps import apps
from django.db.models import F,Q

def article_search_view(request):
    query= request.GET.get("q")
    qs = Articles.objects.search(query)
    context = {
        "object_list":qs
    }
    return render(request,"cutting_app/search.html",context=context)

def article_create_view(request):
    form = ArticleForm(request.POST or None )
    context = {
        "form":form,
    }
    if form.is_valid(): 
        article_obj = form.save()
        return HttpResponseRedirect(reverse("article-detail" ,args={"slug":article_obj.slug}))
    context["list_objects"] = Articles.objects.all()
  
        # context['form'] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # print(title)
        # article_obj = Articles.objects.create(title=title,content=content)
    return render(request, "cutting_app/articles.html",context=context)
def article_detail_view(request,slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Articles.objects.get(slug=slug)
        except Articles.DoesNotExist:
            raise Http404
        except Articles.MultipleObjectsReturned:
            article_obj = Articles.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object":article_obj,
    }
    return render(request,"cutting_app/detail.html",context=context)
def stock(request):
    form = StockForm(request.POST or None)
    context = {
        "stockform":form,
    }
    if form.is_valid():
        stock_id = form.cleaned_data.get("stock_id")
        stock_name = form.cleaned_data.get("stock_name")
        notes = form.cleaned_data.get("notes")
        stock_obj = Stock.objects.create(stock_id=stock_id,stock_name=stock_name, note=notes)
    return render(request,"cutting_app/Stock.html", context=context
    
    )
    
