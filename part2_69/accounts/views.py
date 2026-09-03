from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, ProfileForm
from django.urls import reverse_lazy

from .models import Profile
# Create your views here.
# FBV
def home_view(request):
    context ={}
    if request.user.is_authenticated:
        #ดึง profile
        context['profile'] = Profile.objects.filter(user=request.user).first()
        print(context)
    return render(request, "accounts/home.html", context)

#CBV
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("profile_edit")

    def get_object(self):
        return self.request.user.profile

class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

class MyLogoutView(LogoutView):
    next_page = 'home'

