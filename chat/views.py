from django.shortcuts import render
import sys
import MeCab
from .forms import PatternForm
from .models import Pattern
from chat.script.chat import chat_func
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class ChatView(LoginRequiredMixin, FormView):
    def get(self, request, *args, **kwargs):
        return render(request, 'chat/chat.html', {'user_name': request.user})

    def post(self, request, *args, **kwargs):
        content = {
            'message': chat_func(request, request.POST.get('message')),
            'user_name': request.user,
        }
        return render(request, 'chat/chat.html', content)


chat = ChatView.as_view()


class RegiptnView(LoginRequiredMixin, FormView):
    def get(self, request, *args, **kwargs):
        form = PatternForm(user=self.request.user)
        return render(request, 'chat/regi_ptn.html', {'form': form, 'user_name': request.user})

    def post(self, request, *args, **kwargs):
        form = PatternForm(request.POST, user=self.request.user)
        if form.is_valid():
            pattern = form.save(commit=False)
            pattern.user = request.user
            pattern.save()
            content = {
                'form': PatternForm(user=self.request.user),
                'user_name': request.user,
                'success_message': 'パターン：' + form.cleaned_data['pattern_text']
                                   + '　返答：' + form.cleaned_data['output_text']
                                   + '　の内容でパターンを保存しました'
            }
            return render(request, 'chat/regi_ptn.html', content)
        else:
            return render(request, 'chat/regi_ptn.html', {'form': form, 'user_name': request.user})


regi_ptn = RegiptnView.as_view()


class CheckptnView(LoginRequiredMixin, FormView):
    def get(self, request, *args, **kwargs):
        content = {
            'user_name': request.user,
            'patterns': Pattern.objects.filter(user__username=request.user),
        }
        return render(request, 'chat/check_ptn.html', content)

    def post(self, request, *args, **kwargs):
        return render(request, 'chat/chat.html',)


check_ptn = CheckptnView.as_view()
