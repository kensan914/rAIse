from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')

    def post(self, request):
        return render(request, 'home/home.html')


home = HomeView.as_view()


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('chat:lab')
    template_name = '../templates/registration/signup.html'


signup = SignUpView.as_view()


class MyPageView(LoginRequiredMixin, View):
    def get(self, request):
        content = {
            'user_name': request.user
        }
        return render(request, 'accounts/mypage.html', content)

    def post(self, request):
        return render(request, 'accounts/mypage.html')


mypage = MyPageView.as_view()