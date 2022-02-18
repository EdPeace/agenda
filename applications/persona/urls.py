from django.urls import path, re_path

from . import views

app_name = 'persona app'

urlpatterns = [
    path('personas/', views.ListaPersonas.as_view(), name='personas'),
    path('api/persona/lista/', views.PersonListApiView.as_view(), ),
    path('lista/', views.PersonListView.as_view(), name='search'),
    path('api/persona/search/<kword>/', views.PersonSearchApiView.as_view(), ),
    path('api/persona/create/', views.PersonCreateApiView.as_view()),
    path('api/persona/detail/<pk>/', views.PersonRetrieveApiView.as_view(),name='detalle'),
    path('api/persona/delete/<pk>/',views.PersonDestroyApiView.as_view()),
    path('api/persona/update/<pk>/',views.PersonUpdateApiView.as_view()),
    path('api/personas/',views.PersonAPILista.as_view()),
    path('api/reuniones/',views.ReunionAPILista.as_view()),
    path('api/reuniones2/',views.ReunionAPILista2.as_view()),
    path('linkinpark/',views.ReunionAPIListaLink.as_view()),
]
