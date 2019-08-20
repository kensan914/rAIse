from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('chat:chat')
    template_name = 'accounts/signup.html'


signup = SignUpView.as_view()


class MyPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        content = {
            'user_name': request.user
        }
        return render(request, 'accounts/mypage.html', content)

    def post(self, request, *args, **kwargs):
        return render(request, 'accounts/mypage.html')


mypage = MyPageView.as_view()