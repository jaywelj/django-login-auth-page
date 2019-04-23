from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def news_list(request):
	return render(request, "news_site/news_list.html")

@login_required(login_url='/login/')
def game_list(request):
	return render(request, "news_site/game_list.html")
