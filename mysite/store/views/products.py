from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from ..models import Product


class ProductListView(ListView):

    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProductListByCategoryView(ListView):

    model = Product
    paginate_by = 100  # if pagination is desiredi
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        qs = Product.objects.filter(category=category_id)
        return qs
    template_name = 'products_by_category.html'



class ProductDetailView(DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

