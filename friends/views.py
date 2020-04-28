from django.shortcuts import render
from django.http import HttpResponse
from .models import friends
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.forms import formset_factory
#from .filters import friendsFilter

def filter(request):

    context = {'AAAA':'AAAA'}
    return render(request, 'cashtreats/stuff.html', {'context':context})




######
class friendPostListView(ListView):
    model = friends
    template_name = 'friends/friends_home.html'
    context_object_name = 'post'  # it takes object in post for
    ordering = ['-date_posted']


class friendPostDetailView(DetailView):
    model = friends
    template_name = 'friends/friends_post_detail.html'


class friendPostCreateView(LoginRequiredMixin, CreateView):
    model = friends
    fields = ['name', 'age', 'activities', 'gender', 'body', 'height', 'fees', 'language','contact', 'email', 'address', 'about', 'photo']
    template_name = 'friends/friends_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)


class friendPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # prevent from unauthorised update
    model = friends
    fields = ['name', 'age', 'activities', 'gender', 'body', 'height', 'fees', 'language','contact', 'email', 'address', 'about', 'photo']
    template_name = 'friends/friends_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class friendPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # prevent from unauthorised update
    model = friends
    template_name = 'friends/friends_post_confirm_delete.html'
    success_url = '/friend-home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

##########################################################################################

# class FriendCreateView(LoginRequiredMixin, CreateView ):
#     model = friends
#     fields = ['name', 'age','title']
#     template_name = 'friends/upload2.html'
#     success_url = 'friends'
#     def form_valid(self, form):
#         form.instance.author = self.request.user #login must be required to run function with author
#         return super().form_valid(form)
#
#
# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'friends/upload2.html'  # Replace with your template.
#     success_url = 'upload2'  # Replace with your URL or reverse().
#
#     def add(request):
#         if request.method == 'POST':  # If the form has been submitted...
#             form = FileFieldForm(request.POST)  # A form bound to the POST data
#             if form.is_valid():
#                 form.save()
#         return HttpResponse('Saved')
#
#
#
#
#
#
# def friends_list(request):
#     if request.method == 'POST':
#         form = formfriends(request.POST or request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Saved')
#     else:
#         form = formfriends()
#     return render(request, 'friends/friends_list.html', {"form":form})
# #
# #
# def friends_details(request):
#     return render(request, 'friends/friends_details.html', {"text":"text"})
