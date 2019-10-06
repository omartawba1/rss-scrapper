from django.http import HttpResponseRedirect
from django.views import View
from scrappers.models import Content


class FavouritesDetailsView(View):
    def dispatch(self, *args, **kwargs):
        """
        Navigate through the class based on the request method
        :param args:
        :param kwargs:
        :return:
        """
        method = self.request.POST.get('_method', '').lower()
        if method == 'post':
            return self.post(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(FavouritesDetailsView, self).dispatch(*args, **kwargs)

    def post(self, request, id):
        """
        Save new favourite
        :param request:
        :param id:
        :return:
        """
        feed = Content.objects.get(pk=id, favourite=False, rss__user=request.user)
        if feed:
            feed.favourite = True
            feed.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def delete(self, request, id):
        """
        Delete favourite
        :param request:
        :param id:
        :return:
        """
        feed = Content.objects.get(pk=id, favourite=True, rss__user=request.user)
        if feed:
            feed.favourite = False
            feed.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
