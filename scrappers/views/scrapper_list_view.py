from django.shortcuts import render, redirect
from django.views import View
from scrappers.forms import RSSPostForm
from scrappers.models import Rss


class ScrapperListView(View):
    def get(self, request):
        """
        List the rss records
        :param request:
        :return:
        """
        data = Rss.objects.filter(user=request.user.id)
        form = RSSPostForm()
        return render(request, 'rss/index.html', {'data': data, 'form': form})

    def post(self, request):
        """
        Store new rss record.
        :param request:
        :return:
        """
        form = RSSPostForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            rss = Rss(url=url, user=request.user)
            rss.save()
        else:
            form = RSSPostForm()

        return redirect('rss.index')
