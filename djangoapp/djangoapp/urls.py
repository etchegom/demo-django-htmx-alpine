from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", include("contact.urls")),
    path("modal/", include("modal.urls")),
    path("movie/", include("movie.urls")),
]
