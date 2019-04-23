from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
			login(request, new_user)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('news_list')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

