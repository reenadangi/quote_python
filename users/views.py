from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}, you can login now')
            print("*"*40,messages)
            return redirect("register")
    else:
        form=UserRegisterForm()
        # login_form=auth_views.LoginView.as_view()
        
    login_form = AuthenticationForm()
    context={'form':form,'login_form':login_form}
    return render(request,'users/register.html',context)

def signin(request):
    print("in login****")
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect("quotes")
            else:
                messages.warning(request, "Invalid username or password.")
        else:
            messages.warning(request, "Invalid username or password.")
    return redirect('register')
    
def signout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('register')

def edit_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            # check for email
            user_with_email=User.objects.all().filter(email=request.user.email).exclude(id=request.user.id)
            print(user_with_email)
            if(user_with_email):
                form = UserUpdateForm(instance=request.user)
                context={'form':form}
                messages.warning(request, f'Email Already exist')
                return render(request,'users/editprofile.html/',context)
            else:

                form.save()
                messages.success(request, f'Your account is updated')
                return redirect('quotes')
    else:
        form = UserUpdateForm(instance=request.user)

    context={'form':form}
    return render(request,'users/editprofile.html/',context)

def editProfile(request):
    # p_form=UserUpdateForm()
    
    # user={'user':User.objects.get(id=request.user.id)}
    # print(context, "profile updating")
    # print(f"update {request.user.id} {user.id}")

    # form=UserRegisterForm()
    #     # login_form=auth_views.LoginView.as_view()
        
    # login_form = AuthenticationForm()
    # context={'form':p_form}
    # user.first_name=request.POST['first_name']
    # user.last_name=request.POST['last_name']
    # user.emailaddress= request.POST['email']
    # user.save() 
    return render(request,"quotes")
    
    