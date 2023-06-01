from django_filters import rest_framework
from reviews.models import Title


class TitleFilter(rest_framework.FilterSet):

    name = rest_framework.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )
    year = rest_framework.NumberFilter(
        field_name='year',
        lookup_expr='icontains'
    )
    category = rest_framework.CharFilter(
        field_name='category__slug',
        lookup_expr='exact'
    )
    genre = rest_framework.CharFilter(
        field_name='genre__slug',
        lookup_expr='exact'
    )

    class Meta:
        model = Title
        fields = ('name', 'year', 'category', 'genre',)
