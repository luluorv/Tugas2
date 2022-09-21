from django.shortcuts import render
from mywatchlist.models import WatchlistItem

# TODO: Create your views here.

def show_watchlist(request):
    watchlistitem = WatchlistItem.objects.all()
    watched = WatchlistItem.objects.filter(watched = True).count()
    not_watched = WatchlistItem.objects.filter(watched = False).count()
    
    context = {
    'list_watchlist': watchlistitem,
    'nama': 'Clarissa Thea Aryanto',
    'id': '2106634673'
    }
    return render(request, "mywatchlist.html", context)