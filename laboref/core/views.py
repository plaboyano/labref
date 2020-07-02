from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "Laboref"})


class AboutView(TemplateView):
    template_name = "core/about-us.html"
