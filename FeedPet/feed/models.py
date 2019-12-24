# feed/models.py
from datetime import date
from django.db import models
from master.models import Master, Pet
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'fname'),
    ('2', 'fitem'),
    ('3', 'fusage1'),
    ('4', 'flegalname'),
)


class Feed(models.Model):
    fname = models.CharField(max_length=20)
    fitem = models.CharField(max_length=10)
    fmat = models.CharField(max_length=500)
    fnut = models.CharField(max_length=100)
    fusage1 = models.CharField(max_length=50)
    fusage2 = models.CharField(max_length=50)
    fusage3 = models.CharField(max_length=50)
    flegalname = models.CharField(max_length=20)
    master_feed = models.ManyToManyField(
        Master, through='Favor_feed', related_name='master_feed')
    pet_feed = models.ManyToManyField(
        Pet, through='Record', related_name='pet_feed')

    def __str__(self):
        return self.fname


class Record(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    water = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    time = models.DateField(default=date.today)

    def __str__(self):
        return self.time


class Favor_feed(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


def query_feed_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Feed.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                   Q(fname__icontains=search_value) |
                                   Q(fitem__icontains=search_value) |
                                   Q(fusage1__icontains=search_value) |
                                   Q(flegalname__icontains=search_value))

    count = queryset.count()

    if length == -1:
        queryset = queryset.order_by(order_column)
    else:
        queryset = queryset.order_by(order_column)[start:start + length]

    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }
