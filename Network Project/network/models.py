from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Newpost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.IntegerField(default=0, blank=True, null=True, editable=False)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return {
            "id": self.id,
            "user": self.user,
            "post": self.post,
            "time": self.time.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes,
            "liked": self.liked
        }

class Profile(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seguindo") 
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seguido")

    def __str__(self):
        return f"Following: {self.follower}, being followed {self.following}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Newpost, on_delete=models.PROTECT)
