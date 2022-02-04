from django.urls import path
from . import views

app_name = 'films'
urlpatterns = [
    path('films/', views.FilmsListView.as_view(), name='films_all'),
    path('films/<int:id>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('films/<int:id>/update/', views.FilmsUpdateView.as_view(), name='film_update'),
    path('films/<int:id>/delete/', views.FilmsDeleteView.as_view(), name='film_delete'),
    path('add-film/', views.FilmsCreateView.as_view(), name='add_film'),
]
