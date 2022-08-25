from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return HttpResponseRedirect(reverse('emp'))
    return render(request,"accounts/register.html",{
        "form":form
    })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    return render(request,'accounts/logout.html')



def login_view(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("garment:create"))
        
        else:
            messages.success(request, "There are an error login ....")
            return redirect('login')
            # Return an 'invalid login' error message       .

    else:
        return render(request, 'accounts/login.html',{})


