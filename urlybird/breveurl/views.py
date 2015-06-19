from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View, DetailView, UpdateView, ListView, CreateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator
from hashids import *

from .models import Bookmark

# Create your views here.
class LoginRequiredMixin(object):
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class IndexView(ListView):
    header = "Hola Muchacho"
    template_name = 'breveurl/index.html'
    model = Bookmark
    context_object_name = 'bookmark_list'

def takemethere(request, urlid):
    if request.method=="GET":
        print("We got {}".format(urlid))
        tinyurl = Bookmark.objects.get(breveurl = urlid)
        return redirect(tinyurl.url, permanent=False)
            
class UserView(LoginRequiredMixin, DetailView):
    header = "BreveURL - Home"
    model = User
    template_name = 'breveurl/home.html'
    def get_object(self):
        return get_object_or_404(User, pk = self.request.user.id)

    def get_queryset(self):
        pass
    
class BookMarkMixin(object):
    fields = ('url', 'description', 'tags')
    
    @property # set the message for each action
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        form.instance.user = User.objects.get(id=self.request.user.id)        
        form.instance.breveurl = self.shortenURL()
        return super(BookMarkMixin, self).form_valid(form)

    def shortenURL(self):
        from hashids import Hashids
        hashids = Hashids(salt="Kilimokwanza", min_length=4)
        lastentry = Bookmark.objects.latest('id')
        
        if lastentry is None:
            lastentry.id = 0
        return hashids.encrypt(lastentry.id+1)
        
    
class BookmarkCreateView(LoginRequiredMixin, BookMarkMixin, CreateView):
    model = Bookmark
    success_msg = 'Bookmark added successfully'
    template_name = 'breveurl/create_bookmark.html'
    success_url = '/breveurl'
    
class BookmarkUpdateView(LoginRequiredMixin, BookMarkMixin, UpdateView):
    model = Bookmark
    success_msg = "Bookmark updated successfully"
    template_name = 'breveurl/update_bookmark.html'


class BreveURLRedirectView():
    permanent = False
    query_string = True
    #pattern-name = 'hello'
    #hola = Bookmark.objects.get()
    
    
    
