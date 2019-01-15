# Link de plantillas de vistas basadas en clases (CBV)
# https://ccbv.co.uk/
# Link vistas basadas en clases documentación oficialself.
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/
# Link de clases de tipo TEMPLATES
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#templateview

from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "core/home.html"

    # Esta es una forma de pasar un diccionario de contexto.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Mi titulo a través de un diccionario'
        return context


class SamplePageView(TemplateView):
    template_name = "core/sample.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo': 'Titulo de la página sample'})
