from rest_framework import viewsets
from recipes.models import (Ingredient, Tag, Recipe,
                            IngredientAmount, Favorite, ShoppingList)
from users.models import User, Subscription
from .serializers import (
    IngredientSerializer,
    TagSerializer,
    RecipeSerializer,
    IngredientAmountSerializer,
    FavoriteSerializer,
    ShoppingListSerializer,
    UserSerializer,
    SubscriptionSerializer
)
from djoser.views import UserViewSet
from api.filters import IngredientFilter, RecipeFilter

import io
from api.paginations import CustomPagination
from django.db.models import Sum
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (SAFE_METHODS, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from api.permissions import AuthorOrReadOnly
from api.serializers import (FavoriteCreateDeleteSerializer,
                             IngredientSerializer, RecipeCreateSerializer,
                             RecipeReadSerializer,
                             ShoppingCartCreateDeleteSerializer,
                             SubscribeCreateSerializer, SubscribeSerializer,
                             TagSerializer)
from recipes.models import (AmountIngredient, Favorite, Ingredient, Recipe,
                            ShoppingCart, Tag)
from users.models import Subscription, User

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.select_related("author").prefetch_related(
        "tags", "ingredients")
    permission_classes = [AuthorOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeReadSerializer
        return RecipeCreateSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientAmountViewSet(viewsets.ModelViewSet):
    queryset = IngredientAmount.objects.all()
    serializer_class = IngredientAmountSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class UserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
