from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetListView, SnippetDetailView, UserListView, UserDetailView

app_name = "snippets"

urlpatterns = [
    path("users/", UserListView.as_view(), name="list_users"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("snippets/", SnippetListView.as_view(), name="snippet_list"),
    path("snippets/<int:pk>/", SnippetDetailView.as_view(), name="snippet_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
