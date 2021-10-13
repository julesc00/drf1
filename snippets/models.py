from django.db import models

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments.styles import get_all_styles
from pygments import highlight


LEXERS = [lexer for lexer in get_all_lexers() if lexer[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    """Create the snippet object."""

    title = models.CharField(max_length=100, blank=True, default="")
    owner = models.ForeignKey("auth.User", related_name="snippets", on_delete=models.CASCADE)
    highlighted = models.TextField()
    code = models.TextField(blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default="python")
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, default="friendly")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

    def save(self, *args, **kwargs):
        """Use the 'pygments' library to create a highlighted HTML representation
        of the code snippet.

        We'll need to update our database tables when finished editing:

        rm -f db.sqlite3
        rm -r snippets/migrations
        python manage.py makemigrations snippets
        python manage.py migrate

        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True,
                                  **options)

        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
