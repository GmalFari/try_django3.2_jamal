from django.urls import path
from .views import (
    # update,
    article_detail_view,
    detail_view,
    # home,
    stock,
    article_create_view
    # fabric_view,
    # created_view,
)

app_name = 'garment'
urlpatterns = [
    # path('',home,name="home"),
    path('create',article_create_view,name="create"),
    path("article/<slug:slug>",article_detail_view,name="article-detail"),
    path('stock',stock,name="stock"),
    # path('update/<str:tablename>/<int:id>',update, name="updatepage"),
    # path('created/<str:tablename>/<int:id>',created_view, name='created'),
    # path('emp',emp_view,name="emp"),
    # path('fabric',fabric_view,name='fabric'),

]