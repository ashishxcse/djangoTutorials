from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import EditProfileForm
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return redirect("home")

        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})
    else:
        return redirect('dashboard')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/dashboard.html')
    else:
        return redirect("login")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form':form})

def password_reset(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                
                update_session_auth_hash(request, form.user) # for not log out after password change

                return render(request, 'accounts/password_reset_complete.html')
            
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'accounts/password_reset.html', {'form':form})
    else:
        return redirect('login')
    
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
            
        form = EditProfileForm(instance=request.user)
        return render(request,'accounts/edit_profile.html', {'form':form})
    else:
        return redirect('login')
    


def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "accounts/profile.html")
        
    
    else:
        return redirect("login")

