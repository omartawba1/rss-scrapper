from django.shortcuts import render, redirect
from django.views import View
from scrappers.models import Content, Rss


class ScrapperDetailsView(View):
    def dispatch(self, *args, **kwargs):
        """
        Navigate through the class based on the request method
        :param args:
        :param kwargs:
        :return:
        """
        method = self.request.POST.get('_method', '').lower()
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(ScrapperDetailsView, self).dispatch(*args, **kwargs)

    def get(self, request, id):
        """
        Display rss content
        :param request:
        :param id:
        :return:
        """
        data = Content.objects.filter(rss=id, rss__user=request.user)
        return render(request, 'rss/details.html', {'data': data})

    def delete(self, request, id):
        """
        Delete Rss record
        :param request:
        :param id:
        :return:
        """
        Rss.objects.filter(pk=id, user=request.user).delete()
        return redirect('rss.index')
