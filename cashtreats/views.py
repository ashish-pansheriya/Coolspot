from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import cashtreats
from application.models import databank
from rest_framework import viewsets
from .serializers import rest

class restframe(viewsets.ModelViewSet):
    queryset = databank.objects.all()
    serializer_class = rest



def home(request):
    post = databank.objects.all()
    return render(request, 'cashtreats/home.html', {'post':post})


#
# def upload(request,user_id):
#     for afile in request.FILES.getlist('files'):
#         user = UserProfile.objects.get(user_id=user_id)
#         pic = UserProfile(request.POST or request.FILES)
#         pic.image = afile
#         pic.save()
#         redirect('upload')
#     else:
#
#         return render(request,'cashtreats/upload.html')