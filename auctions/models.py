from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class category(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    
class listings(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('closed', 'Closed'),
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    img = models.URLField()
    starting_bid = models.IntegerField(null=True)
    stat = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    kategory = models.ForeignKey(category, on_delete=models.SET_NULL,blank=True, null=True,default=None,  related_name="listing_category")

    #category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, related_name="all_category_items")

    def __str__(self):
        return f"{self.user.username} listed {self.title}"



class bid(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid_on = models.ForeignKey(listings, on_delete=models.CASCADE, related_name="all_bids")
    bid = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} bid on {self.bid_on.title}"
    
class comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentor")
    commented = models.ForeignKey(listings, on_delete=models.CASCADE, related_name="all_comments")
    comment = models.TextField()

class watchlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="want")
    item = models.ForeignKey(listings, on_delete=models.CASCADE, related_name="wants")