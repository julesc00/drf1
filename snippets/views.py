from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


User = get_user_model()


@api_view(["GET"])
def api_root_view(request, format=None):
    return Response({
        "users": reverse("snippets:user-list", request=request, format=format),
        "snippets": reverse("snippets:snippet-list", request=request, format=format)
    })


class UserListView(generics.ListAPIView):
    """List all users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """List a specific user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetListView(generics.ListCreateAPIView):
    """List all snippets, or create a new snippet."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a snippet instance."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class SnippetHighlightView(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
