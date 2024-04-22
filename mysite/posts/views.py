from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Post
#Post, Comments, Report, Save
from .serializers import UserSerializer, PostSerializer
# , PostSerializer, CommentsSerializer, ReportSerializer, SaveSerializer
from django.db import IntegrityError

class AddUser(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Create a new user object using validated data from the serializer
            print(request.data)
            user = serializer.save()
            # Serialize the newly created user object
            new_serializer = self.serializer_class(user)
            # Return the serialized data with 200 OK status
            return Response(new_serializer.data, status=status.HTTP_200_OK)
        # If serializer is not valid, return errors with 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUser(APIView):
    def put(self, request, username_in):
        try:
            user = User.objects.get(username = username_in)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUser(APIView):
    def delete(self, request, username_in):
        try:
            user = User.objects.get(username=username_in)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_200_OK)

class UserPosts(APIView):
    def get(self, request, username_in):
        try:
            # Retrieve all posts belonging to the user with the specified user_id
            user = User.objects.get(username=username_in)
            posts = Post.objects.filter(UserID=user.id)
            # Serialize the posts data
            serialized_posts = PostSerializer(posts, many=True).data
            return Response(serialized_posts, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# Post Views
class AddPost(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditPost(APIView):
    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePost(APIView):
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






