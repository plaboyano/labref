from django.views.generic import ListView
from applications.animal.models import Animal


class IndexListView(ListView):
    template_name = "adoptions/adoptions.html"
    model = Animal


"""
class IndexListView(ListView):
    template_name = "core/home.html"
    model = ItemSlider

    items = ItemSlider.objects.all()
    news = News.objects.all()
    first_three_animals = Animal.objects.all().order_by('-created')[:3]

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(IndexListView, self).get_context_data(**kwargs)
        context.update({'itemslider_list': self.items, 'news_list': self.news, 'animals': self.first_three_animals})
        return context


"""