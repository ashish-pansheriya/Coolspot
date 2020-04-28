from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.forms import formset_factory


######
class eventPostListView(ListView):
    model = events
    template_name = 'events/events_home.html'
    context_object_name = 'post'  # it takes object in post for
    ordering = ['-date_posted']


class eventPostDetailView(DetailView):
    model = events
    template_name = 'events/events_post_detail.html'


class eventPostCreateView(LoginRequiredMixin, CreateView):
    model = events
    fields = ['title', 'location', 'types', 'topic', 'starts', 'ends', 'image', 'description', 'organiser',
              'description2', 'tickets', 'contact', 'email']
    template_name = 'events/events_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)


class eventPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # prevent from unauthorised update
    model = events
    fields = ['title', 'location', 'types', 'topic', 'starts', 'ends', 'image', 'description', 'organiser',
              'description2', 'tickets', 'contact', 'email']
    template_name = 'events/events_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class eventPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # prevent from unauthorised update
    model = events
    template_name = 'events/events_post_confirm_delete.html'
    success_url = '/events-home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def events(request):
    return HttpResponse('Events Page')
