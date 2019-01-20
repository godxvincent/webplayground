from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm
from django.urls import reverse_lazy

# Create your views here.


# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages': pages})

class PageViewList(ListView):
    model = Page
    # Aqui no se ha indicado cual es el template por lo que el busca algo
    # del estilo Modelo_List como nombre del template


# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page': page})

class PageViewDetail(DetailView):
    model = Page
    # Al usar DetailView la clase va a buscar un template con nombre modelo_detail.


class PageViewCreate(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']

    # Esta es una forma de sobre escribir la variable success_url pero para
    # ahorrase el metodo hay otra forma
    # def get_success_url(self):
    #     return reverse('pages:pages')
    success_url = reverse_lazy('pages:pages')


class PageViewUpdate(UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageViewDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
