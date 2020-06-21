from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/products/')
    icon = models.ImageField(upload_to='images/products/icons/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')

