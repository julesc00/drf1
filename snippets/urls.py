from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import (SnippetListView,
                            SnippetDetailView,
                            UserListView,
                            UserDetailView,
                            api_root_view,
                            SnippetHighlightView)

app_name = "snippets"

urlpatterns = format_suffix_patterns([
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("snippets/", SnippetListView.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", SnippetDetailView.as_view(), name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", SnippetHighlightView.as_view(), name="snippet-highlight"),
    path("", api_root_view),
])
