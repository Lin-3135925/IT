from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login after successful registration
            login(request, user)
            # redirect to home/browse page
            return redirect('browse') 
    else:
        # GET request, show empty form
        form = UserCreationForm()
        
    return render(request, 'accounts/signup.html', {'form': form})