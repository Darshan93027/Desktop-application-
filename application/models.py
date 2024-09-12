from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User 

class Signup(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    signup_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    user1 = models.ForeignKey(User, related_name='user1_chats', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2_chats', on_delete=models.CASCADE, null=True, blank=True)
    user1_message = models.TextField(null=True, blank=True)  # Add this if not already in your model
    user2_message = models.TextField(null=True, blank=True)  # Add this if not already in your model
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.user1} and {self.user2}"