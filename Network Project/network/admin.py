from django.contrib import admin

from .models import User,Newpost, Profile, Like
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password")

class NewpostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "likes", "liked", "time")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "following")

class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post")

admin.site.register(User,UserAdmin)
admin.site.register(Newpost,NewpostAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Like,LikeAdmin)