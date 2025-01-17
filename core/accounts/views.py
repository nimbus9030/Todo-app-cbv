from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from accounts.forms import CustomUserCreationForm

# Create your views here.


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "email", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("task-list")


class RegisterPage(FormView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task-list")
        return super(RegisterPage, self).get(*args, **kwargs)
