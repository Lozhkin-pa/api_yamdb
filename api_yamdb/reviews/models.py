from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название категории'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг',
        help_text='Слаг категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название жанра'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг',
        help_text='Слаг жанра'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название произведения',
        db_index=True,
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        help_text='Год выпуска',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание произведения',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр',
        help_text='Жанр произведения',
        blank=True,
        db_index=True,
    )
    category = models.ForeignKey(
        Category,
        related_name='titles',
        verbose_name='Категория',
        help_text='Категория произведения',
        db_index=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name