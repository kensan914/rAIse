from django.shortcuts import render, redirect
import sys
import MeCab
from django.contrib.auth.decorators import login_required
from .forms import PatternForm
from chat.script.chat import chat


@login_required
def ChatView(request):
    if request.method == "POST":
        form = PatternForm(request.POST)
        if 'registrate' in request.POST:
            if form.is_valid():
                pattern = form.save(commit=False)
                pattern.user = request.user
                pattern.save()
                return redirect('chat:chat')
        elif 'send' in request.POST:
            form = PatternForm()
            d = {
                'message': chat(request, request.POST.get('message')),
                'form': form,
            }
            return render(request, 'chat/home.html', d)
    else:
        form = PatternForm()
    return render(request, 'chat/home.html', {'form': form})
