# Generated by Django 4.2.6 on 2024-01-07 17:33

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmountIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(help_text='Enter amount of ingredient', validators=[django.core.validators.MinValueValidator(limit_value=1, message='At least 1!'), django.core.validators.MaxValueValidator(limit_value=32767, message='No more than 32767!')], verbose_name='Amount of ingredient')),
            ],
            options={
                'verbose_name': 'Ingredient from recipe',
                'verbose_name_plural': 'Ingredients from recipe',
                'ordering': ('recipe',),
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date of addition')),
            ],
            options={
                'verbose_name': 'Favorite recipe',
                'verbose_name_plural': 'Favorite recipes',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter ingredient name', max_length=200, verbose_name='Ingredient name')),
                ('measurement_unit', models.CharField(help_text='Enter measurement unit', max_length=200, verbose_name='Measurement unit')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter recipe name', max_length=200, verbose_name='Recipe name')),
                ('text', models.TextField(help_text='Enter recipe text', verbose_name='Recipe text')),
                ('image', models.ImageField(help_text='Upload recipe image', upload_to='recipes/images/', verbose_name='Recipe image')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date')),
                ('cooking_time', models.PositiveSmallIntegerField(help_text='Enter cooking time in minutes', validators=[django.core.validators.MinValueValidator(limit_value=1, message='At least 1 minute!'), django.core.validators.MaxValueValidator(limit_value=32767, message='No more than 32767 minutes!')], verbose_name='Cooking time')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter tag name', max_length=200, unique=True, verbose_name='Tag name')),
                ('slug', models.SlugField(help_text='Enter tag slug', max_length=200, unique=True, verbose_name='Tag slug')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Choose color for tag', image_field=None, max_length=7, samples=None, unique=True, verbose_name='HEX-code for color')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='recipes.recipe', verbose_name='Recipe')),
            ],
            options={
                'verbose_name': 'Recipe in shopping cart',
                'verbose_name_plural': 'Recipes in shopping cart',
            },
        ),
    ]
