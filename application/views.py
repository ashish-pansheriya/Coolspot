from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import databank
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.forms import formset_factory
#from 
# from another comments
def home(request):
    users = {
        'post': databank.objects.all()
    }

    return render(request, 'home.html', users)


# check for logged user to update their profile and to see all their profile post
class PostListView(ListView):
    model = databank
    template_name = 'buy&sell/post_home.html'
    context_object_name = 'post' #it takes object in post for
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = databank
    template_name = 'buy&sell/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView ):
    model = databank
    fields = ['title', 'category', 'content', 'price', 'location', 'contact', 'email', 'photo']
    template_name = 'buy&sell/post_form.html'

    def form_valid(self, form):
 #       ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)

        form.instance.author = self.request.user #login must be required to run function with author
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView ): # prevent from unauthorised update
    model = databank
    fields = ['title', 'price', 'content', 'location', 'photo']
    template_name = 'buy&sell/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user #login must be required to run function with author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView ): # prevent from unauthorised update
    model = databank
    template_name = 'buy&sell/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
