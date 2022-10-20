from django.urls import path
from .views import (
    article_detail_view,
    article_search_view,
    stock,
    article_create_view
)

app_name = 'garment'
urlpatterns = [
    # path('',home,name="home"),
    path('create',article_create_view,name="create"),
    path('articles/',article_search_view,name="search"),
    path("article/<slug:slug>",article_detail_view,name="article-detail"),
    path('stock',stock,name="stock"),
    # path('update/<str:tablename>/<int:id>',update, name="updatepage"),
    # path('created/<str:tablename>/<int:id>',created_view, name='created'),
    # path('emp',emp_view,name="emp"),
    # path('fabric',fabric_view,name='fabric'),

]