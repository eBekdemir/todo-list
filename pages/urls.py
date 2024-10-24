from django.urls import path
from django.views.generic.base import RedirectView
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, Login, UserRegisterView, set_theme
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', RedirectView.as_view(url='list/'), name='home'),
    path('signup', UserRegisterView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('list/', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('set-theme/<str:theme>/', set_theme, name='set_theme'),
]