from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from ..models import Category

class CategoryListView(ListView):

    model = Category
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CategoryDetailView(DetailView):

    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

