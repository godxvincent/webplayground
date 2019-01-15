from django.urls import path
# Para usar las clases se importan directamente.
# from . import views
from .views import HomePageView, SamplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    # path('', views.home, name="home"),
    # path('sample/', views.sample, name="sample"),
]
