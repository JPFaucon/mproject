from django.shortcuts import render

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['app'] = "home"
        return context