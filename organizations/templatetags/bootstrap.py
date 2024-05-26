from django import template

register = template.Library()


# @register.filter(name="add_class")
# def add_class(field, css_class):
#     return field.as_widget(attrs={"class": css_class})


@register.filter(name="add_class")
def add_class(value, arg):
    """
    Add a CSS class to the given value.

    Example usage:
    {{ form.field_name|add_class:"form-control" }}
    """
    css_classes = value.field.widget.attrs.get("class", "")
    if css_classes:
        css_classes += f" {arg}"
    else:
        css_classes = arg
    value.field.widget.attrs["class"] = css_classes
    return value
