from django.contrib import admin

from .models import User,Listing, Bid, Comment, Watchlist
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password")

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "seller", "item", "price", "category", "image", "time", "closed")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing", "time", "bid_price")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing", "comment", "time")

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing")

admin.site.register(User,UserAdmin)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Bid,BidAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Watchlist,WatchlistAdmin)