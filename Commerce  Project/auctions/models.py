from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

# model for listings
class Listing(models.Model):

    CATEGORIES = [
        ("CLOT", "Clothes"),
        ("BOOK", "Books"),
        ("ELEC", "Electronics"),
        ("TOYS", "Toys"),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    category = models.CharField(max_length=4, choices=CATEGORIES, default="CLOT")
    image = models.ImageField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Auction id: {self.id}, the item: {self.item}, the price is {self.price} and the seller is: {self.seller}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    bid_price = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return f"{self.user} bid {self.bid_price} $ for the {self.listing}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.comment} for the {self.listing}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,)

    def __str__(self):
        return f"user {self.user} watchlist {self.listing}"