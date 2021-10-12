from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import snippet_list_view, snippet_detail_view

app_name = "snippets"

urlpatterns = [
    path("snippets/", snippet_list_view, name="snippet_list"),
    path("snippets/<int:pk>/", snippet_detail_view, name="snippet_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
