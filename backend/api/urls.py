from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import (
    IngredientViewSet,
    TagViewSet,
    RecipeViewSet,
    IngredientAmountViewSet,
    FavoriteViewSet,
    ShoppingListViewSet,
    UserViewSet,
    SubscriptionViewSet)

router = DefaultRouter()


router.register(r'users', UserViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients_amount', IngredientAmountViewSet, basename='ingredients_amount')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'shopping_cart', ShoppingListViewSet, basename='shopping_cart')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
