from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormView
from omdb_fixtures_loader import loader

from .forms import MovieSearchForm


class MovieSearchFormView(FormView):
    template_name = "search_movie.html"
    form_class = MovieSearchForm
    success_url = reverse_lazy("movie")


@require_http_methods(["POST"])
def search_movie(request):
    search = request.POST.get("search")
    media_type = request.POST.get("media_type")

    if not search:
        return HttpResponse("Error 400: the search text can not be empty")
    if not media_type:
        media_type = "movie"

    try:
        hits = list(
            loader.search_and_fetch(
                api_key=settings.OMDB_API_KEY, search=search, media_type=media_type
            )
        )
    except loader.LoaderError:
        hits = []

    return HttpResponse(
        content=get_template("search_movie_list.html").render(
            {"search": search, "media_type": media_type, "hits": hits}
        )
    )
