from cmath import inf
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid, Comment, Watchlist

class CreateListing(forms.ModelForm):
    item = forms.CharField(label="", required=True)
    description = forms.CharField(label="", widget=forms.Textarea())
    price = forms.DecimalField(label="", required=True, widget=forms.NumberInput())
    category = forms.ChoiceField(required=True, choices=Listing.CATEGORIES)

    item.widget.attrs.update({"placeholder": "Item Name", "size": "50","class": "form-control" })
    description.widget.attrs.update({"placeholder": "Describe your product","class": "form-control","rows": "12","cols": "48"})
    price.widget.attrs.update({"placeholder": "Initial Price","min": 0.01, "max": inf,"class": "form-control", "size": "50"})

    class Meta:
        model = Listing
        fields = ["item", "price", "description", "category", "image"]

class NewBidForm(forms.ModelForm):
    bid_price = forms.DecimalField(label="", required=True, widget=forms.NumberInput(
        attrs={"placeholder": "Bid Price","min": 0.01, "max": inf,"class": "form-control", "size": "10"}))
    class Meta:
        model = Bid
        fields = ["bid_price"]

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={"placeholder": "Make your comment","class": "form-control","rows": "3"}))
    class Meta:
        model = Comment
        fields = ["comment"]

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def new_listing(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = user
            listing.item = request.POST.get("item")
            listing.description = request.POST.get("description")
            listing.category = request.POST.get("category")
            listing.price = request.POST.get("price")
            listing.image = request.FILES.get("image")
            listing.save()
            return redirect(reverse("index"))
        else:
            return render(request, "auctions/new_listing.html", {
                "form": form
            })
    else:
        return render(request, "auctions/new_listing.html", {
            "form": CreateListing()
        })

def listing_page(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    comments = Comment.objects.filter(listing=listing_id)
    bid_amount = Bid.objects.filter(listing=listing_id).count()
    highest_bid = Bid.objects.filter(listing=listing_id).order_by('-bid_price').first()
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        if not listing.closed:

            if request.user.is_authenticated:
                if request.POST.get("button") == "Watchlist": 
                    if not user.watchlist.filter(listing = listing):
                        watchlist = Watchlist(
                            user = user,
                            listing = listing
                        )
                        watchlist.save()
                    else:
                        watchlist = Watchlist.objects.filter(
                            user = user,
                            listing = listing
                        )
                        watchlist.delete()
                    return redirect("listing_page", listing.id)
                    
                price = float(request.POST.get("bid_price"))
                if user.username != listing.seller.username:
                    if listing.price >= price:
                        return render(request, "auctions/listing_page.html", {
                                "listing": listing,
                                "message": "Your Bid should be higher than the Current one.",
                                "comments": comments,
                                "bid_amount": bid_amount,
                                "bid_form": NewBidForm(),
                                "comment_form": CommentForm()
                        })
                    else:
                        form = NewBidForm(request.POST)
                        if form.is_valid():
                            new_bid = Bid(
                                listing = listing, 
                                user=user, 
                                bid_price=price)
                            new_bid.save()
                            listing.price = price
                            listing.save()
                        else:
                            return render(request, 'auctions/listing_page.html', {
                                        "form": form })

            return render(request, "auctions/listing_page.html", {
                    "listing": listing,
                    "comments": comments,
                    "message": "Your bid is the highest bid",
                    "bid_amount": bid_amount,
                    "bid_form": NewBidForm(),
                    "comment_form": CommentForm()
                })
        else:
            watchlist = Watchlist.objects.filter(
                    user = user,
                    listing = listing
                    )
            watchlist.delete()
            if highest_bid is not None:
                winner = highest_bid.user
                return render(request, "auctions/closed_listing.html", {
                        "highest_bid": highest_bid,
                        "winner": winner,
                        "listing": listing})
            return redirect(reverse("index"))
    else:
        if highest_bid is None:
            return render(request, "auctions/listing_page.html", {
                "listing": listing,
                "comments": comments,
                "message": "No bids have been made",
                "bid_amount": bid_amount,
                "bid_form": NewBidForm(),
                "comment_form": CommentForm()
                })
        else:
            return render(request, "auctions/listing_page.html", {
                "listing": listing,
                "comments": comments,
                "message": "Highest bid made by " + highest_bid.user.username,
                "bid_amount": bid_amount,
                "bid_form": NewBidForm(),
                "comment_form": CommentForm()
                })


@login_required
def addcomment(request, listing_id):
    user = User.objects.get(username = request.user)
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = request.POST.get("comment")
            comment = Comment(
                user = user,
                comment = comment,
                listing = listing
            )
            comment.save()
            return redirect("listing_page", listing.id)

@login_required  
def watchlist(request):
    user = User.objects.get(username=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": user.watchlist.all()
    })

@login_required 
def endlisting(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    user = User.objects.get(username = request.user)
    highest_bid = Bid.objects.filter(listing=listing_id).order_by('-bid_price').first()
    if request.POST.get("button") == "Close" and user.username == listing.seller.username:
        listing.closed = True
        listing.save()

    if highest_bid is not None:
        winner = highest_bid.user
        return render(request, "auctions/closed_listing.html", {
                "highest_bid": highest_bid,
                "listing": listing,
                "winner": winner})
    else:
        return render(request, "auctions/closed_listing.html", {
            "highest_bid": highest_bid,
            "listing": listing})

def categories(request, category):
    listings = Listing.objects.filter(category=category, closed=False)
    categorieslist = Listing.CATEGORIES
    categoryname = [x[1] for x in categorieslist if x[0] == category][0]
    if category is not None:
        return render(request, "auctions/categories.html", {
            "categoryname":categoryname,
            "listings":listings,
            "category": category,
        })