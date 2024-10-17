from django import template


register = template.Library()

a1 = "Редиска"
a2 = "редиска"

a = [a1, a2]

@register.filter()
def currency(value):
    value = value.split()
    for a_ in a:
        if a_ in value:
            for _a in a_[1:-0]:
                _a = "*"
    value = " ".join(value)
    return value


