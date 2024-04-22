from rest_framework import serializers
from .models import User, Post, Comments, Report
# , Comments, Report, Save

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'gender']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'UserID', 'description', 'liked', 'status']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'UserID', 'PostID', 'comment']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'UserID', 'PostID', 'reason']

# class SaveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Save
#         fields = ['id', 'UserID', 'PostID']