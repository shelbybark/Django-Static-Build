from django import template
from django.template.defaultfilters import stringfilter
import urlparse

register = template.Library()

@register.filter(name='navurl')
@stringfilter
def navurl(value,request):
    current_url = request.META['PATH_INFO']
    item_url = urlparse.urlparse(value)[2]
    class_name = ''
    if item_url == current_url:
        class_name = 'selected'
    else:
        if item_url and current_url.count(item_url) > 0:
            class_name = 'ancestor'
    return class_name
navurl.is_safe = True