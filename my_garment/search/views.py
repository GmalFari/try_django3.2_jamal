from django.shortcuts import render
from cutting_app.models import Article
from recipes.models import Recipe
# Create your views here.

SEARCH_TYPE_MAPPING = { 
    'articles':Article,
    'aticle':Article,
    'recipes':Recipe,
    'recipe':Recipe,
}

def search_view(request):
    query = request.GET.get('q')
    search_type =request.GET.get('type')
    Klass = Recipe
    if search_type in SEARCH_TYPE_MAPPING.keys():
        Klass = SEARCH_TYPE_MAPPING[search_type]
    qs = Klass.objects.search(query=query)
    context = {
        'queryset':qs,
    }
    template ="search/results-view.html"
    if request.htmx:    
        context['queryset'] = qs[:5]
        template ="search/partials/result.html"
    return render(request,template,context)   
    