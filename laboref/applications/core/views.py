from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ItemSlider, News, Welcome
from applications.animal.models import Animal

"""
class IndexView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "Laboref"})
"""


class AboutView(TemplateView):
    template_name = "core/about-us.html"


class IndexListView(ListView):
    template_name = "core/home.html"
    model = ItemSlider

    items = ItemSlider.objects.all()
    news = News.objects.all()
    welcome = Welcome.objects.last()

    first_three_animals = Animal.objects.all().order_by('-created')[:3]

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(IndexListView, self).get_context_data(**kwargs)
        context.update(
            {
                'itemslider_list': self.items,
                'news_list': self.news,
                'animals': self.first_three_animals,
                'welcome': self.welcome,
            }
        )
        return context

