from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_html(request):
    watchlistitem = WatchlistItem.objects.all()
    watched = WatchlistItem.objects.filter(watched = True).count()
    not_watched = WatchlistItem.objects.filter(watched = False).count()
    count = watched >= not_watched


    context = {
    'list_watchlist': watchlistitem,
    'nama': 'Clarissa Thea Aryanto',
    'id': '2106634673',
    'watched_a_lot': count
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")