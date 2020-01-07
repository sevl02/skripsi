from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    # def in_groups(u):
    #     if u.is_authenticated():
    #         if bool(u.groups.filter(name__in=group_names)):
    #             return True
    #     return False

    # return user_passes_test(in_groups, login_url='403')
    def in_group(u):
        return u.is_active and (u.is_superuser or bool(u.groups.filter(name__in=group_names)))
    return user_passes_test(in_group)
    
@group_required('students', 'teachers')
def index(request):
    return render(request, 'userweb/index.html')
