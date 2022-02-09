from django.urls import path

from . import views

urlpatterns = [
    path("", views.MovieSearchFormView.as_view(), name="movie"),
    path("search", views.search_movie, name="movie_search"),
]
