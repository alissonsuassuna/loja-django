from django.views.generic import ListView, DetailView, TemplateView
from .models import *


class IndexView(ListView):
    model = Produto
    template_name = 'main/index.html'
    context_object_name = 'produtos'


class ProdutoView(DetailView):
    model = Produto
    template_name = 'main/produto.html'
    context_object_name = 'produto'