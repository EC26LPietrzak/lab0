from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def strona_glowna(request):
    return HttpResponse(
        "<h1>Laboratorium 0</h1>"
        "<p>Chyba dziala</p>"
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', strona_glowna),
]