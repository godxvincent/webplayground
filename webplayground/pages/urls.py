from django.urls import path
from .views import PageViewList, PageViewDetail, PageViewCreate

page_urlpatterns = ([
    path('', PageViewList.as_view(), name='pages'),
    # El primary key debe ser modificado para que el parametro recibido es PK
    # y el nombre de la pagina se debe llamar slug
    path('<int:pk>/<slug:slug>/', PageViewDetail.as_view(), name='page'),
    path('create/', PageViewCreate.as_view(), name='create'),
], 'pages')
