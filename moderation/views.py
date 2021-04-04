from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied


def is_moderator(user):
    """This method is used to create a decorator that gives access to a view only
        if the user belongs to the group 'moderators'.
    """
    if user.groups.filter(name='moderators').exists():
        return True
    else:
        raise PermissionDenied()


@login_required
@user_passes_test(is_moderator)
def moderation_home(request):
    return HttpResponse('this is moderation response')
