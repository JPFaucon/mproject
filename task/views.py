from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Task
from .forms import TaskForm

class IndexView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Task
    template_name = "task/index.html"
    context_object_name = 'tasks'
    permission_required = 'task.task_management'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        context['app'] = "task"
        return context

def create(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        Task.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            assignee=form.cleaned_data['assignee']
        )
    
    return HttpResponseRedirect(reverse('task:index'))

def delete(request, id):
    Task.objects.filter(id=id).delete()

    return HttpResponseRedirect(reverse('task:index'))