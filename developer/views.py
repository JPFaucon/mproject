from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Developer
from .forms import ShortDeveloperForm
from task.forms import TaskForm

# def index(request):
#     context = {
#         'developers': Developer.objects.all(),
#         'form': DeveloperForm,
#     }

#     return render(request, 'developer/index.html', context)

class DevDetailVue(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = 'developer/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DevDetailVue, self).get_context_data(**kwargs)
        context['form'] = TaskForm(initial={'assignee': context['developer']})
        context['app'] = "developer"
        field = context['form'].fields['assignee']
        field.widget = field.hidden_widget()
        return context

# def detail(request, developer_id):
#     developer = get_object_or_404(Developer, pk=developer_id)
#     return render(request, 'developer/detail.html', {'developer': developer})

class IndexView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = "developer/index.html"
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ShortDeveloperForm
        context['app'] = "developer"
        return context

def create(request):
    form = ShortDeveloperForm(request.POST)

    if form.is_valid():
        Developer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
        )

    # Developer.objects.create(
    #     first_name=request.POST['first_name'],
    #     last_name=request.POST['last_name']
    # )
    
    return HttpResponseRedirect(reverse('developer:index'))

def delete(request, id):
    Developer.objects.filter(id=id).delete()

    return HttpResponseRedirect(reverse('developer:index'))