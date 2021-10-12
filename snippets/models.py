from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [lexer for lexer in get_all_lexers() if lexer[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    """Create the snippet object."""

    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField(blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default="python")
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, default="friendly")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

