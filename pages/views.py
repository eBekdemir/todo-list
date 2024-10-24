from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["tasks"] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        query = self.request.GET.get('q') or ''
        if query:
            context['tasks'] = context['tasks'].filter(title__icontains=query)
        return context
    


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task_create.html"
    fields = [
        'title',
        'description',
        'complete',
        'dead_line'
    ]

    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_update.html"
    fields = [
        'title',
        'description',
        'complete',
        'dead_line'
    ]    

    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    context_object_name = 'task'

    success_url = reverse_lazy('task_list')

class Login(LoginView):
    success_url = reverse_lazy('task_list')
    template_name = 'login.html'

    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('task_list')
    
class UserRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm

    success_url = reverse_lazy('login')
    def get(self, *args, **kwargs):
        # is_authenticateds
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(UserRegisterView, self).get(*args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
def set_theme(request, theme):
    if theme in ['1', '2', '3']:
        request.session['theme'] = theme  # Store the theme in the session
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect back to the previous page