from django.db import models

from colorfield.fields import ColorField

from django.core.validators import RegexValidator, MinValueValidator

from users.models import User


class Ingredient(models.Model):
    """Ingredient model."""
    name = models.CharField(
        verbose_name='ingredient name',
        null=False,
        blank=False,
        unique=True,
        max_length=250,
    )
    measurement_unit = models.CharField(
        verbose_name='measure unit',
        null=False,
        blank=False,
        unique=False,
        max_length=10,
    )

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.measurement_unit}'


class Tag(models.Model):
    """Tag model."""
    name = models.CharField(
        verbose_name='tag name',
        null=False,
        blank=False,
        unique=True,
        max_length=50
    )
    color = ColorField(
        verbose_name='tag color in hex',
        null=False,
        blank=False,
        unique=True,
        max_length=10,
        format='hex',
        default='#FF0000',
        validators=[RegexValidator(
            regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
            message='Цвет тега должен быть в формате hex (#FFFFFF или #FFF)',
            code='invalid_color')]
    )
    slug = models.SlugField(
        verbose_name='tag slug',
        null=False,
        blank=False,
        unique=True,
        max_length=25,
    )

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name', 'color'],
                                    name='unique_tag_name_color'),
            models.UniqueConstraint(fields=['name', 'slug'],
                                    name='unique_tag_name_slug'),
        ]

    def __str__(self):
        return f'Tagname: {self.name}, tagslug: {self.slug}'


class Recipe(models.Model):
    """Recipe model."""
    name = models.CharField(
        verbose_name='recipe name',
        null=False,
        blank=False,
        unique=True,
        max_length=150,
        db_index=True
    )
    text = models.TextField(
        verbose_name='recipe description',
        null=False,
        blank=False,
        unique=False
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='cooking time in minutes',
        null=False,
        blank=False,
        unique=False,
        validators=[MinValueValidator(
            limit_value=1,
            message='at least one minute')
        ]
    )
    image = models.ImageField(
        verbose_name='dish image',
        null=False,
        blank=False,
        upload_to='backend_media/',
    )
    pub_date = models.DateTimeField(
        verbose_name='publication date',
        null=False,
        blank=False,
        unique=False,
        auto_now_add=True
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='recipe author',
        null=False,
        blank=False,
        unique=False,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    tag = models.ManyToManyField(
        to=Tag,
        verbose_name='recipe tag',
        blank=False,
        unique=False,
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        to=Ingredient,
        verbose_name='recipe ingredients',
        blank=False,
        unique=False,
        related_name='recipes',
        through='IngredientAmount'
    )

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(fields=['name', 'author'],
                                    name='unique_recipe_author'),
        ]

    def __str__(self):
        return f'{self.name} - {self.pub_date}'


class IngredientAmount(models.Model):
    """Ingredient Amount model."""
    recipe = models.ForeignKey(
        to=Recipe,
        verbose_name='recipe',
        on_delete=models.CASCADE,
        related_name='ingredients_in_recipe'
    )
    ingredient = models.ForeignKey(
        to=Ingredient,
        verbose_name='ingredient',
        on_delete=models.CASCADE,
        related_name='recipes_with_ingredient'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='ingredient amount in recipe',
        null=False,
        blank=False,
        unique=False,
        validators=[MinValueValidator(
            limit_value=1,
            message='at least one ingredient amount'
        )]
    )

    class Meta:
        verbose_name = 'ingredients in recipe'
        verbose_name_plural = 'ingredients in recipe'
        ordering = ['recipe']

    def __str__(self):
        return f'{self.recipe} - {self.ingredient} - {self.amount}'


class Favorite(models.Model):
    """Favorite recipes model."""
    recipe = models.ForeignKey(
        to=Recipe,
        verbose_name='favorite recipe',
        null=True,
        blank=True,
        related_name='recipe_fans',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User,
        verbose_name='user with favorite recipe',
        null=True,
        blank=True,
        related_name='favorite_recipes',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'favorite recipes'
        verbose_name_plural = 'favorite recipes'
        ordering = ['user']
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'user'],
                                    name='unique_favorite'),
        ]

    def __str__(self):
        return f'{self.user} loves: {self.recipe}.'


class ShoppingList(models.Model):
    """Shopping list model."""
    recipe = models.ForeignKey(
        to=Recipe,
        verbose_name='recipe for shopping list',
        null=True,
        blank=True,
        related_name='shopping_users',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User,
        verbose_name='user with shopping list',
        null=True,
        blank=True,
        related_name='recipes_for_shopping',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'recipes for shopping list'
        verbose_name_plural = 'recipes for shopping list'
        ordering = ['user']
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'user'],
                                    name='unique_shopping_list'),
        ]

    def __str__(self):
        return f'{self.user} added {self.recipe} in shopping list.'
