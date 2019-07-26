from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    pic = models.ImageField(upload_to = 'images', blank=True)
    rank = models.IntegerField(default=0)
    cite = models.CharField(max_length=200, blank=True)
    News = 'NE'
    Politics= 'PO'
    Sports = 'SP'
    Local = 'LO'
    Opinion = 'OP'
    Health = 'HE'
    Entertainment = 'EN'
    art_cats = (
        (News, 'News'),
        (Politics, 'Politics'),
        (Sports, 'Sports'),
        (Local, 'Local'),
        (Opinion, 'Opinion'),
        (Health, 'Health'),
        (Entertainment, 'Entertainment')
    )
    art_cat = models.CharField(max_length=2, choices=art_cats, default=News)

    def __str__(self):
        return self.headline
