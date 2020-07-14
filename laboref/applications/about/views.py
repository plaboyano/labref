from django.views.generic import TemplateView
from .models import Collaborator


class IndexView(TemplateView):
    template_name = "about/about-us.html"

    model = Collaborator
    collaborators = Collaborator.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'collaborators_list': self.collaborators})
        return context
