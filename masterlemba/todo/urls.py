from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("criar/", TodoCreateView.as_view(), name="todo_create"),
    path("alterar/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("deletar/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("completar/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
   
    #login
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

   
    
]
