from django.urls import path

from . import views

app_name = 'veranstaltung'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:id>', views.VeranstaltungsView.as_view(), name='detail'),
]