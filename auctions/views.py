from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Max

from .models import User, listings, bid, comments, category, watchlist


def index(request):
    if request.method == "POST":
        ...
    else:
        return render(request, "auctions/index.html", { 
            "listings": listings.objects.all()
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

def create_listing(request):
    if request.method == 'POST':
        title = request.POST["Title"]
        user = request.POST["user"]
        userr = User.objects.get(username=user)
        description = request.POST["description"]
        img = request.POST["img"]
        bid_value = request.POST["bid"]
        cat_name = request.POST["selected_category"] 
        print(f"Received category name: {cat_name}")
        cat = category.objects.get(name=cat_name)
        new_listing = listings(
            user=userr,
            title=title,
            description=description,
            starting_bid=bid_value,
            img=img, 
            kategory=cat
        )
        new_listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        current_user = request.user
        return render(request, "auctions/list_item.html", {
            "user": current_user, "category": category.objects.all()
        })
    
def listing_detail(request, listing_id):
    listing = listings.objects.get(id=listing_id)
    total_bids = bid.objects.filter(bid_on=listing_id).count()
    all_bids = bid.objects.filter(bid_on=listing_id)
    if all_bids:
        highest_bidder = 0
        highest_bid = bid.objects.filter(bid_on=listing_id).aggregate(max_integer=Max('bid'))['max_integer']
        highest_bidder = bid.objects.get(bid=highest_bid)
        winner = highest_bidder.user.username
    else:
        highest_bid = listing.starting_bid
        highest_bidder=0
        winner=0
    all_cemments = listing.all_comments.all()
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user) 
        watch_list = watchlist.objects.filter(user=request.user, item=listing).first() 
        if request.method == "POST":
            if  request.POST.get("add_watch", None):
                new_watch = watchlist(
                    user=request.user,
                    item=listing
                )
                new_watch.save()  
                return HttpResponseRedirect(reverse("listing_detail", args=[listing_id]))
            elif request.POST.get("remove_watch", None):
                item = watchlist.objects.filter(item=listing).first() 
                item.delete()
                return HttpResponseRedirect(reverse("listing_detail", args=[listing_id])) 
            elif request.POST.get("bid_placed", None):
                bid_price = request.POST["bid_placed"] 
                new_bid = bid(
                    user=request.user,
                    bid_on=listing,
                    bid=bid_price
                )
                new_bid.save()
                return HttpResponseRedirect(reverse("listing_detail", args=[listing_id])) 
            elif request.POST.get("close_auction", None):
                listing.stat = 'closed'
                listing.save()
                return HttpResponseRedirect(reverse("listing_detail", args=[listing_id]))
            elif request.POST.get("comment", None):
                cmnt = request.POST["comment"]
                listing = listings.objects.get(id=listing_id)
                new_comment = comments(
                    user=User.objects.get(username=request.user),
                    commented=listing,
                    comment=cmnt
                )
                new_comment.save()
                return HttpResponseRedirect(reverse("listing_detail", args=[listing_id]))
        else:
            return render(request, "auctions/listing.html", {
                "listing": listing, "watchlist": watch_list, "total_bids": total_bids, "all_bids": all_bids,
                "highest_bid": highest_bid, "highest_bidder": highest_bidder, 'winner': winner , "user":user, 
                "comments":all_cemments
            })
    else:
        return render(request, "auctions/listing.html", {
                "listing": listing, "total_bids": total_bids, "all_bids": all_bids,
                  "highest_bid": highest_bid, "highest_bidder":highest_bidder, "comments":all_cemments, 'winner': winner 
            })

def watch_list(request):
    if request.method == 'POST':
        ...
    else:
        current_user = request.user

        return render(request, "auctions/watchlist.html", {
               "item": current_user.want.all(), "listings": listings
        })
    
def categorys(request):
    return render(request, "auctions/categorys.html", {
               "category": category.objects.all()
        })
def each_category(request, cate):
    category_names = category.objects.all()
    return render(request, "auctions/each_category.html", {
               "listings":  listings.objects.filter(kategory__name=cate), "category":category_names
        }) 