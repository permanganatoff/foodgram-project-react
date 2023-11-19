from rest_framework import serializers
from recipes.models import (Tag, Ingredient, IngredientAmount,
                            Recipe, Favorite, ShoppingList)
from users.models import User

from djoser.serializers import UserSerializer

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, status


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id','email','username','first_name', 'last_name', 'password')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'text', 'image', 'pub_date',
                  'author', 'tag', 'ingredients')

