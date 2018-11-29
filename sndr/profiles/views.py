from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from profiles.forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView , DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from profiles.models import User
from django.contrib.auth import logout
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.birth_date = form.cleaned_data.get('birth_date')
            user.contact    = form.cleaned_data.get('contact')
            user.email      = form.cleaned_data.get('email')
            user.gender     = form.cleaned_data.get('gender')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserDetailView(DetailView,LoginRequiredMixin):
    model = User
    template = "properties/user_detail.html"
