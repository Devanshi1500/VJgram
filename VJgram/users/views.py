from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_id = User.objects.get(username = username)
            m = Profile(user=user_id)
            m.save()
            messages.success(request,f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data.get('username')
            user_id = User.objects.get(username = username)
            image = p_form.cleaned_data.get('image')
            gender = p_form.cleaned_data.get('gender')
            birth_date = p_form.cleaned_data.get('birth_date')
            Profile.objects.filter(user = user_id).update(image = image,gender = gender, birth_date = birth_date)
            email = u_form.cleaned_data.get('email')
            User.objects.filter(username = username).update(username = username,email=email)

            messages.success(request,f'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'users/profile.html',context = context)

def home(request):
    return render(request,'VJgramapp/mainpage.html')

def about(request):
    return render(request,'users/about.html')
