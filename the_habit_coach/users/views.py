from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from habits.models import Habit, HabitLog
from django import forms

def register(request):
    if  request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form' : form})


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

class HabitListView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = 'users/dashboard.html'
    context_object_name = 'habits'


class HabitDetailView(LoginRequiredMixin, DetailView):
    model = Habit

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["habit_logs"] = self.get_object().habitlog_set.all()
        return context


class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    fields = ['name', 'category', 'daily_or_weekly', 'duration']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HabitLogCreateView(LoginRequiredMixin, CreateView):
    model = HabitLog
    fields = ['date', 'value']

    def form_valid(self, form):
        form.instance.habit_id = self.kwargs['pk']
        print(self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.widgets.DateInput(attrs={'type': 'date'})
        return form

class HabitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Habit
    fields = ['name', 'category', 'daily_or_weekly', 'duration']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        habit = self.get_object()
        if self.request.user == habit.user:
            return True
        return False


class HabitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Habit
    success_url = '/'
    def test_func(self):
        habit = self.get_object()
        if self.request.user == habit.user:
            return True
        return False


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'users/home.html')