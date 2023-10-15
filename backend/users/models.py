from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    email = models.EmailField(
        verbose_name='user email',
        blank=False,
        null=False,
        unique=True,
        max_length=150,
        db_index=True
    )
    username = models.CharField(
        verbose_name='user login name',
        blank=False,
        null=False,
        unique=True,
        max_length=150
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='user first name'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='user last name'
    )
    password = models.CharField(
        max_length=150,
        verbose_name='user password'
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username']

    def __str__(self):
        return self.username


class Subscription(models.Model):
    """Subscription model."""

    subscriber = models.ForeignKey(
        to=User,
        verbose_name='subscriber',
        on_delete=models.CASCADE,
        related_name='authors'
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='author',
        on_delete=models.CASCADE,
        related_name='subscribers'
    )

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscription'
        ordering = ['id']
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'subscriber'],
                name='unique_subscription'),
            models.CheckConstraint(
                check=~models.Q(subscriber=models.F('author')),
                name='self_subscription_prohibited')
        )

    def __str__(self):
        return f'{self.subscriber} subscribed to {self.author}.'
