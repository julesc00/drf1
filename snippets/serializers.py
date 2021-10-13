from django.contrib.auth import get_user_model

from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
        read_only_fields = ("id",)


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer the snippet object."""
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "owner", "title", "code", "linenos", "language", "style"]
        read_only_fields = ("id",)
