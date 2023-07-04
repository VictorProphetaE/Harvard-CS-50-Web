import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django import forms
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import User,Newpost,Profile,Like

class NewpostForm(forms.ModelForm):
    post = forms.CharField(label="", widget=forms.Textarea(
        attrs={"placeholder": "Make your post","class": "form-control","rows": "3"}))
    class Meta:
        model = Newpost
        fields = ["post"]

def index(request):
            
    posts = Newpost.objects.all().order_by("-time")
    
    for post in posts:
        post.likes = Like.objects.filter(post=post.id).count()
        post.save()
    
    paginator = Paginator(posts, 10)
    if request.GET.get("page") != None:
        try:
            posts = paginator.page(request.GET.get("page"))
        except:
            posts = paginator.page(1)
    else:
        posts = paginator.page(1)

    return render(request, "network/index.html",{
        "posts":posts,
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def newpost(request):
    user = User.objects.get(username = request.user)
    if request.method == "POST":
        form = NewpostForm(request.POST)
        if form.is_valid():
            post = request.POST.get("post")
            post = Newpost(
                user = user,
                post = post,
            )
            post.save()
            return redirect(reverse("index"))
        else:
            return render(request, "network/newpost.html", {
                "form": form
            })
    else:
        return render(request, "network/newpost.html", {
        "newpost_form": NewpostForm()
    })

def userprofile(request, user_id):
    try:
        user = User.objects.get(id = user_id)
        seguido = Profile.objects.filter(following = user).count()
        seguindo = Profile.objects.filter(follower = user).count()
        followi = Profile.objects.filter(follower = request.user, following = user)
        posts = Newpost.objects.filter(user=user.id).order_by("-time")
    except:
        return render(request, "network/login.html")

    if request.method == "POST":
        if not followi:
            profile = Profile.objects.create(
                        follower = request.user,
                        following = user
                    )
            profile.save()
            follow = True
        else:
            profile = Profile.objects.get(
                        follower = request.user,
                        following = user
                    )
            profile.delete()
            follow = False           
        return redirect("userprofile", user.id)    
    else:
        for post in posts:
            post.likes = Like.objects.filter(post=post.id).count()
            post.save()
            paginator = Paginator(posts, 10)
        if request.GET.get("page") != None:
            try:
                posts = paginator.page(request.GET.get("page"))
            except:
                posts = paginator.page(1)
        else:
            posts = paginator.page(1)
        if not followi:
            follow = True
        else:
            follow = False     
                
        return render(request, "network/userprofile.html", {
            "user": user,
            "posts":posts,
            "follow": follow,
            "followers": seguido,
            "following": seguindo,
            "followi":followi,
        })

@login_required
def following(request):
    try:
        following = Profile.objects.filter(follower = request.user).values('following_id')
        posts = Newpost.objects.filter(user__in = following).order_by("-time")
    except:
        return render(request, "network/login.html")

    for post in posts:
        post.likes = Like.objects.filter(post=post.id).count()
        post.save()

    paginator = Paginator(posts, 10)
    if request.GET.get("page") != None:
        try:
            posts = paginator.page(request.GET.get("page"))
        except:
            posts = paginator.page(1)
    else:
        posts = paginator.page(1)
    return render(request, "network/following.html", {
        "posts": posts,
        })

@csrf_exempt
@login_required
def edit(request, post_id):
    try:
        post = Newpost.objects.get(id = post_id)
    except Newpost.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("post") is not None:
            post.post = data["post"]
        post.save()
        return JsonResponse({}, status=201)
    return JsonResponse({ "error": "GET or PUT request required." }, status=400)

@csrf_exempt
@login_required
def postlike(request):
    try:
        post_id = request.POST.get("id")
        post = Newpost.objects.get(id = post_id)
    except Newpost.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "POST":
        if post.liked  == True:
            Like.objects.filter(user=request.user, post=post).delete()
            post.likes = Like.objects.filter(post=post).count()
            post.liked = False
        else:
            Like.objects.create(user=request.user, post=post)
            post.likes = Like.objects.filter(post=post).count()
            post.liked = True
        post.save()
        return JsonResponse({"counte": post.likes, "likes":post.liked, "status": 201})

    return JsonResponse({"error": "GET or PUT request required." }, status=400)