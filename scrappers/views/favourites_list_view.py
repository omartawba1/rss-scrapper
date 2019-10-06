from django.shortcuts import render
from django.views import View

from scrappers.models import Content


class FavouritesListView(View):
    def get(self, request):
        """
        List the favourites
        :param request:
        :return:
        """
        data = Content.favourites.filter(rss__user=request.user)
        return render(request, 'rss/details.html', {'data': data})
