from django.contrib import admin
from basic.models.models import Topping, Pizza, Zakaz
from basic.models.main import Category, Product

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Zakaz)

admin.site.register(Category)
admin.site.register(Product)
