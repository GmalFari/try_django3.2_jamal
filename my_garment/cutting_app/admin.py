from django.contrib import admin

from .models import  Article

from .models import Stock
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display= ['id','title','slug','timestamp','updated']
    search_fields = ['title','content']
admin.site.register(Article,ArticleAdmin)
admin.site.register(Stock)
