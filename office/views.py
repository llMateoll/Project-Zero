from django.shortcuts import render , redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from .models import Level

# Create your views here.

#@method_decorator(login_required, name='dispatch')
def Office(request):
    profile = Profile.objects.filter(referenceID=request.user.profile.id)
    socio = Profile.objects.filter(id=request.user.profile.referenceID)
    level = Level.objects.all()
    return render(request,'office/office.html', {'profile':profile,'socio':socio, 'level':level})

# def OfficeLevel(request):
#     level = Level.objects.filter(level)
#     #profile = model_to_dict(request.user.profile)
#     return render(request, 'office/office.html', {'level':level})
