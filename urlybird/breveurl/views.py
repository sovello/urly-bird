from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View, DetailView, UpdateView, ListView, CreateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator
from hashids import *
import json

from .models import Bookmark
from click.models import Click
# Create your views here.
class LoginRequiredMixin(object):
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class IndexView(ListView):
    header = "Hola Muchacho"
    template_name = 'breveurl/index.html'
    model = Bookmark
    paginate_by = 10
    context_object_name = 'bookmark_list'

    
class UserView(LoginRequiredMixin, ListView):
    header = "BreveURL - Home"
    model = User
    template_name = 'breveurl/home.html'
    paginate_by = 10
    context_object_name = 'bookmark_list'
    
    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(User, pk = self.request.user.id)
        return super(UserView,self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['current_user'] = self.object
        return context
    
    def get_queryset(self):
        return self.object.bookmark_set.all();

    
class BookMarkMixin(object):
    fields = ('url', 'description', 'tags')
    
    @property # set the message for each action
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        if not self.request.user.is_authenticated():
            form.instance.user = User.objects.get(username='breveurl')
        else:
            form.instance.user = User.objects.get(id=self.request.user.id)
        form.instance.breveurl = self.shortenURL()
        return super(BookMarkMixin, self).form_valid(form)

    def shortenURL(self, anonymous = True):
        from hashids import Hashids
        import random
        hashids = Hashids(salt="Kilimokwanza", min_length=4)
        
        if len(Bookmark.objects.all()) == 0:
            lastentry = Bookmark()
            lastentry.id = 0
        else:
            lastentry = Bookmark.objects.latest('id')
        return hashids.encrypt(lastentry.id+1)

    
class BookmarkCreateView(BookMarkMixin, CreateView):
    model = Bookmark
    success_msg = 'Bookmark added successfully'
    template_name = 'breveurl/create_bookmark.html'
    success_url = '/breveurl/home/'

    
class BookMarkCreateAnonymous(BookMarkMixin, CreateView):
    def form_valid(self, form):
        form.instance.user = AnonymousUser.objects.get()
        form.instance.breveurl = shortenURL()
        return super(BookMarkCreateAnonymous, self).form_valid(form)

    
class BookmarkUpdateView(LoginRequiredMixin, BookMarkMixin, UpdateView):
    model = Bookmark
    success_msg = "Bookmark updated successfully"
    template_name = 'breveurl/update_bookmark.html'
    success_url = '/breveurl/home/'

def delete_bookmark(request):    
    if request.method == 'POST':        
        bookmark_id = request.POST.get('the_bookmark') # this was set in the jQuery
        response_data = {} # preparing the response data
        bookmark = Bookmark(id=bookmark_id, user=request.user)
        bookmark.delete()

        response_data['messages'] = 'Bookmark delete successfully!'
        response_data['delete_node'] = bookmark_id
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"That was another post"}),
            content_type="application/json"
        )

    
class BreveURLRedirectView():
    permanent = False
    query_string = True
    
        
def takemethere(request, urlid):
    from datetime import datetime
    if request.method=="GET":
        print("We got {}".format(urlid))
        tinyurl = Bookmark.objects.get(breveurl = urlid)
        click = Click()
        click.bookmark = tinyurl
        click.ip_address = request.META['REMOTE_ADDR']
        click.accessed_at = datetime.now()
        if request.user.is_anonymous():
            click.user = User.objects.get(username = 'breveurl')
        else:
            click.user = request.user
        click.save()
        return redirect(tinyurl.url, permanent=False)
