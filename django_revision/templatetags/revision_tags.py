from django import template
from django_revision import site_revision


register = template.Library()


@register.simple_tag
def revision():
    """Returns the git site_revision."""
    return '{}'.format(site_revision.revision)


@register.simple_tag
def revision_tag():
    """Returns the git site_revision."""
    return '{}'.format(site_revision.tag)


@register.simple_tag
def revision_branch():
    """Returns the git site_revision."""
    return '{}'.format(site_revision.branch)


@register.simple_tag
def revision_commit():
    """Returns the git site_revision."""
    return '{}'.format(site_revision.commit)
