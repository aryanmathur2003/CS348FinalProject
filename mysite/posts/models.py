from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    gender = models.CharField(max_length=5, null=True)

class Post(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null = True)
    description = models.CharField(null = True, max_length=200)
    liked = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

class Comments(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', null = True)
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment', null = True)
    comment = models.CharField(null = True, max_length=200)

class Report(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report', null = True)
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='report', null = True)
    reason = models.CharField(max_length=200, null=True)

# class Save(models.Model):
#     UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save', null = True)
#     PostID = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='save', null = True)

