from .models import Article
import django_filters

class ArtFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ['art_cat',]
