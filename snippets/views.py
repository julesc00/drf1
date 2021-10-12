from django.http import Http404

from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import status

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetListView(mixins.ListModelMixin, mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """List all snippets, or create a new snippet."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, generics.GenericAPIView):
    """Retrieve, update or delete a snippet instance."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
