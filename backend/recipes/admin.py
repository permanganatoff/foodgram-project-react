from django.contrib import admin
from .models import (Tag, Ingredient, Recipe,
                     IngredientAmount, Favorite, ShoppingList)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'author')
    search_fields = ('name',)
    list_filter = ('pub_date',)


admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientAmount)
admin.site.register(Favorite)
admin.site.register(ShoppingList)
