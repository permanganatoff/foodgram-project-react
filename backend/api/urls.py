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


router.register('users', UserViewSet)
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet)
router.register('ingredients_amount', IngredientAmountViewSet)
router.register('favorite', FavoriteViewSet)
router.register('shopping_cart', ShoppingListViewSet)
router.register('subscriptions', SubscriptionViewSet)
router.register('ingredients', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
