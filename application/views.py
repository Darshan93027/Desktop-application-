from django.shortcuts import render, redirect

from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Signup
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Chat

from django.db import IntegrityError
from datetime import datetime

from django.shortcuts import render, redirect
from django.conf import settings

from .models import Signup  # Assuming you have a Signup model


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Create a new user in your Signup model
        user = Signup.objects.create(
            fname=fname,
            lname=lname,
            email=email,
            username=username,
            password=password
        )
        
        # Redirect to a success page or login page after signup
        return redirect('login')  # or 'myapp/login.html' if it’s a template

    return render(request, 'myapp/signup.html')



def login_view(request):
    error = None  # Initialize error as None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password exist in the Signup table
        try:
            user = Signup.objects.get(username=username, password=password)
            # If found, redirect to the 'chat' page
            return redirect('chat')  # This will take the user to the chat page
        except Signup.DoesNotExist:
            # If no such user exists, show error
            error = "Invalid username or password."

    # Render the login page with the error message (if any)
    return render(request, 'myapp/login.html', {'error': error})





def index(request):
    return render(request,'myapp/index.html')

def admin_login(request):
    return render(request,'myapp/admin_login.html')

def admin_data(request):
    return render(request,'myapp/admim_data.html')



def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username and password match the predefined values
        if username == 'Darshan' and password == 'darshan@123':
            return redirect('admin_data')
        else:
            error = "Invalid username or password"
    
    return render(request, 'myapp/admin_login.html', {'error': error})

def admin_data(request):
    # Logic for the admin_data view
    return render(request, 'myapp/admin_data.html')





def display_signup_data(request):
    signup_data = Signup.objects.all()
    return render(request, 'myapp/admin_data.html', {'signup_data': signup_data})  # Updated to render the correct template


def main_page(request):
    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        password = request.POST.get('password')
        
        # Validate the chat ID and password
        try:
            chat = Chat.objects.get(chat_id=chat_id, password=password)
            # Redirect to the chat page with the chat ID
            return redirect('chat', chat_id=chat_id)
        except Chat.DoesNotExist:
            error = "Invalid chat ID or password. Please try again."
            return render(request, 'myapp/login_sucess.html', {'error': error})

    return render(request, 'myapp/login_success.html')

def chat(request, chat_id):
    chat = Chat.objects.get(chat_id=chat_id)
    messages = chat.messages.all()  # Assuming a related manager for messages
    
    return render(request, 'chat.html', {'chat': chat, 'messages': messages})

def create_chat_id_password(request):
    if request.method == 'POST':
        # Generate a random Chat ID and Password
        chat_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        # Create a new Chat instance and save it to the database
        chat = Chat.objects.create(chat_id=chat_id, password=password, user1=request.user)

        # Redirect to the chat page or show the Chat ID and Password to the user
        return redirect('main_page')  # Adjust the redirect as needed

    return render(request, 'myapp/login_success.html') 


def help(request):
    return render(request,'myapp/help.html')

def chat(request):
    return render(request,'myapp/chat.html')


@login_required
def chat_view(request):
    user1_chats = Chat.objects.filter(user1=request.user)
    user2_chats = Chat.objects.filter(user2=request.user)

    user1_exists = user1_chats.exists()
    user2_exists = user2_chats.exists()

    if request.method == 'POST':
        message = request.POST['message']
        if 'user1_msg' in request.POST:
            chat = Chat.objects.filter(user1=request.user, user2__isnull=False).first()
            if chat:
                chat.user1_message = message
                chat.save()
        elif 'user2_msg' in request.POST:
            chat = Chat.objects.filter(user2=request.user, user1__isnull=False).first()
            if chat:
                chat.user2_message = message
                chat.save()
        return redirect('msg')

    context = {
        'user1_chats': user1_chats,
        'user2_chats': user2_chats,
        'user1_exists': user1_exists,
        'user2_exists': user2_exists,
    }
    return render(request, 'myapp/msg.html', context)



# yeh code added hai 

def sender_view(request):
    return render(request, 'myapp/sender.html')

def receiver_view(request):
    return render(request, 'myapp/receiver.html')


def gender_view(request):
    return render(request, 'myapp/gender.html')

def choose_view(request):
    return render(request, 'myapp/choose.html')\

def learn_more_view(request):
    return render(request, 'myapp/learn_more.html')