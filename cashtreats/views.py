from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import cashtreats
from application.models import databank
from friends.models import friends
from events.models import events



def home(request):
    eva = events.objects.all()
    if request.GET.get('q'):
        q = request.GET.get('q')
        data = friends.objects.filter(address__icontains=q)
    context = {'eva':eva}

    users = {
        'post': events.objects.all()
    }

    return render(request, 'cashtreats/home.html', users )

def terms(request):

    return render(request, 'cashtreats/terms.html', )


def about(request):
    return render(request, 'cashtreats/about.html', )

def policy(request):
    return render(request, 'cashtreats/policy.html', )

def services(request):
    return render(request, 'cashtreats/services.html', )


