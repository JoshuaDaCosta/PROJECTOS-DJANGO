from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'todo/register.html', {'form': form})

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'
    def get_queryset(self):
        return Todo.objects.filter(usuario=self.request.user)


class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("todo_list")
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    
class TodoUpdateView(UpdateView):
    model=Todo
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("todo_list")
    def get_queryset(self):
        return Todo.objects.filter(usuario=self.request.user)
class TodoDeleteView(DeleteView):
    model=Todo
    success_url=reverse_lazy("todo_list")
    def get_queryset(self):
        return Todo.objects.filter(usuario=self.request.user)
class TodoCompleteView(View):
    def get(self, request, pk):
        todo= get_object_or_404(Todo, pk=pk)
        todo.marcar_completo()
        return redirect("todo_list")
    def get_queryset(self):
        return Todo.objects.filter(usuario=self.request.user)