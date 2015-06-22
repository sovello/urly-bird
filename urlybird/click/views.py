from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from breveurl.models import Bookmark
from .models import Click
from ip2location import IP2Location
import os
from django.conf import settings
# Create your views here.
def stats(request, **kwargs):
    if request.method == "GET":
        bookmarkid = request.GET.get('bookmark')
        year = kwargs['year']
        bookmark = Click.objects.filter(bookmark = bookmarkid)
        counts = len(bookmark)
        database = IP2Location.IP2Location(settings.MEDIA_ROOT[0]+"/IPV4.BIN")
        rec = database.get_all("19.5.10.1")
        print(type(rec))
        return render(request, 'click/stats.html', {"bkmark":bookmark, "geodata":rec, "counts": counts, "year":year})
    
def stats_map(request, bookmark):
    pass

