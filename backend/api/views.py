from rest_framework import viewsets, status
from recipes.models import Ingredient, Tag, Recipe
from users.models import User
from .serializers import IngredientSerializer, TagSerializer, RecipeSerializer
from djoser.views import UserViewSet
from api.paginations import CustomPagination
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from api.serializers import IngredientSerializer, CustomUserSerializer, TagSerializer
from recipes.models import Ingredient, Recipe, Tag
from users.models import User


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    @action(methods=['POST', 'DELETE'], detail=True, permission_classes=[AllowAny],)
    def subscribe(self, request, id=None):
        if request.method == 'POST':
            return Response(data='it was subscribe post', status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            return Response(data='it was subscribe delete', status=status.HTTP_200_OK)
        else:
            raise ValueError

    @action(methods=['GET',], detail=False, permission_classes=[AllowAny],)
    def subscriptions(self, request):
        if request.method == 'GET':
            return Response (data='it was subscriptions get', status=status.HTTP_200_OK)
        else:
            raise ValueError
        

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    @action(methods=['POST', 'DELETE',], detail=True, permission_classes=[AllowAny])
    def favorite(self, request, id=None):
        if request.method == 'POST':
            return Response(data='it was favorite post', status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            return Response(data='it was favorite delete', status=status.HTTP_200_OK)
        else:
            raise ValueError

    @action(methods=['GET',], detail=False, permission_classes=[AllowAny])
    def download_shopping_cart(self, request):
        if request.method == 'GET':
            return Response(data='it was download_shopping_cart get', status=status.HTTP_200_OK)
        else:
            raise ValueError
    
    @action(methods=['POST', 'DELETE',], detail=True, permission_classes=[AllowAny])
    def shopping_cart(self, request, id=None):
        if request.method == 'POST':
            return Response(data='it was shopping_cart post', status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            return Response(data='it was shopping_cart delete', status=status.HTTP_200_OK)
        else:
            raise ValueError


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [AllowAny]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


