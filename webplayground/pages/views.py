from django.views.generic import ListView, DetailView
from .models import Page

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
