import re
from django import template
from django.utils.html import linebreaks
from django.utils.safestring import mark_safe

register = template.Library()

_HTML_TAG_RE = re.compile(
    r'<(p|h[1-6]|ul|ol|li|div|br|strong|em|b|i|a|span|blockquote|table|thead|tbody|tr|td|th|img|hr|section|article)\b',
    re.IGNORECASE,
)


@register.filter(name='blog_content')
def blog_content(value):
    """Render HTML blog content as-is; plain text gets linebreaks."""
    if not value:
        return ''
    text = str(value).strip()
    if _HTML_TAG_RE.search(text):
        return mark_safe(text)
    return linebreaks(text)
