from django.contrib import admin
from company.models import Category, Article, Gallery

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Gallery)