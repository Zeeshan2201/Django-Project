from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

@login_required
def user_chat(request, username):
    # Get the selected user for chat
    try:
        other_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('chat_room')  # Redirect if the user doesn't exist

    # Fetch messages between the logged-in user and the selected user
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')  # Order by timestamp for chronological display

    # Handle message sending
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=other_user, content=content)
            return redirect('user_chat', username=other_user.username)  # Avoid duplicate submissions

    return render(request, 'chat/user_chat.html', {'other_user': other_user, 'messages': messages})


@login_required
def chat_room(request):
    # Fetch all messages and registered users
    messages = Message.objects.all().order_by('timestamp')  # Ensure proper order
    users = User.objects.exclude(id=request.user.id)  # Exclude the logged-in user

    # Handle message sending
    if request.method == "POST":
        content = request.POST.get('content')
        receiver_username = request.POST.get('receiver')  # Get receiver from the form
        if content and receiver_username:
            receiver = User.objects.get(username=receiver_username)
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
    
    return render(request, 'chat/chat_room.html', {'messages': messages, 'users': users})


def home_view(request):
    return render(request, 'chat/home.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Create the user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error during signup: {e}")
            return redirect('chat_room')
    return render(request, 'chat/signup.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('chat_room')  # Redirect to chat room after successful login
            else:
                messages.error(request, "Invalid credentials. Please try again.")  # Show error message
        else:
            messages.error(request, "Invalid form submission.")  # Show error if form is not valid
    else:
        form = AuthenticationForm()  # Instantiate an empty login form

    return render(request, 'chat/login.html', {'form': form})
