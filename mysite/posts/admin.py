from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Post
# , Comments, Report, Save

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'gender')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'UserID', 'description', 'liked', 'status')

# @admin.register(Comments)
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'UserID', 'PostID', 'comment')

# @admin.register(Report)
# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('id', 'UserID', 'PostID',  'reason')

# @admin.register(Save)
# class SaveAdmin(admin.ModelAdmin):
#     list_display = ('id', 'UserID', 'PostID')