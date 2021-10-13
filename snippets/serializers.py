from django.contrib.auth import get_user_model

from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]
        read_only_fields = ("id",)


class SnippetSerializer(serializers.ModelSerializer):
    """Serializer the snippet object."""
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ["id", "owner", "title", "code", "linenos", "language", "style"]
        read_only_fields = ("id",)
