from django.contrib import admin
from .models import Signup, Chat

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'username')
    search_fields = ('fname', 'lname', 'email', 'username')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'user1_message', 'user2_message', 'timestamp')
    search_fields = ('user1__username', 'user2__username', 'user1_message', 'user2_message')
